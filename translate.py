import base64
import hashlib
import hmac
import json
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import format_datetime
from urllib.parse import urlparse
from dotenv import load_dotenv
import os
import requests
from requests import JSONDecodeError


@dataclass
class AliyunMtClient:
    access_key_id: str
    access_key_secret: str
    service_url: str = "http://mt.cn-hangzhou.aliyuncs.com/api/translate/web/ecommerce"
    acs_version: str = "2019-01-02"
    timeout: int = 60

    @staticmethod
    def _md5_base64(body_bytes: bytes) -> str:
        md5_bytes = hashlib.md5(body_bytes).digest()
        return base64.b64encode(md5_bytes).decode("utf-8")

    @staticmethod
    def _hmac_sha1_base64(data: str, key: str) -> str:
        raw = hmac.new(key.encode("utf-8"), data.encode("utf-8"), hashlib.sha1).digest()
        return base64.b64encode(raw).decode("utf-8")

    @staticmethod
    def _gmt_date() -> str:
        # 生成 GMT 时间字符串
        return format_datetime(datetime.now(timezone.utc), usegmt=True)

    def translate(
            self,
            *,
            format_type: str,
            source_language: str,
            target_language: str,
            source_text: str,
            scene: str,
            context: str | None = None,
    ) -> dict:
        """
        调用阿里云机器翻译
        """
        parsed = urlparse(self.service_url)
        host = parsed.netloc
        path = parsed.path  # /api/translate/web/ecommerce

        payload = {
            "FormatType": format_type,
            "SourceLanguage": source_language,
            "TargetLanguage": target_language,
            "SourceText": source_text,
            "Scene": scene,
        }
        if context:
            payload["Context"] = context

        body_str = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
        body_bytes = body_str.encode("utf-8")

        method = "POST"
        accept = "application/json"
        content_type = "application/json;charset=utf-8"  # 文档指定 :contentReference[oaicite:5]{index=5}
        date_gmt = self._gmt_date()
        nonce = str(uuid.uuid4())

        # MD5
        body_md5 = self._md5_base64(body_bytes)

        # stringToSign
        string_to_sign = (
            f"{method}\n"
            f"{accept}\n"
            f"{body_md5}\n"
            f"{content_type}\n"
            f"{date_gmt}\n"
            f"x-acs-signature-method:HMAC-SHA1\n"
            f"x-acs-signature-nonce:{nonce}\n"
            f"x-acs-version:{self.acs_version}\n"
            f"{path}"
        )

        # Signature
        signature = self._hmac_sha1_base64(string_to_sign, self.access_key_secret)

        # Authorization
        authorization = f"acs {self.access_key_id}:{signature}"

        headers = {
            "Accept": accept,
            "Content-Type": content_type,
            "Content-MD5": body_md5,
            "Date": date_gmt,
            "Host": host,
            "Authorization": authorization,
            "x-acs-signature-nonce": nonce,
            "x-acs-signature-method": "HMAC-SHA1",
            "x-acs-version": self.acs_version,
        }

        resp = requests.post(
            self.service_url,
            data=body_bytes,
            headers=headers,
            timeout=self.timeout,
        )

        # 兼容：成功/失败都尽量解析 JSON
        try:
            return resp.json()
        except JSONDecodeError:
            return {
                "http_status": resp.status_code,
                "text": resp.text,
            }

def create_translate_client() -> AliyunMtClient:
    load_dotenv()
    ak = os.getenv('API_KEY')
    sk = os.getenv('SECRET_KEY')

    client = AliyunMtClient(
        access_key_id=ak,
        access_key_secret=sk,
        service_url="http://mt.cn-hangzhou.aliyuncs.com/api/translate/web/ecommerce",
    )
    return client

def main():
    client = create_translate_client()

    result = client.translate(
        format_type="text",
        source_language="zh",
        target_language="en",
        source_text="你好",
        scene="general",
        context="早上我在家里吃了面包",
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
