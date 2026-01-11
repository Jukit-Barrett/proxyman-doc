import os
import shutil
import chardet
import translate
import json

translator = translate.create_translate_client()

def translate_text(content: str) -> str:
    translated = translator.translate(
        format_type="text",
        source_language="en",
        target_language="zh",
        source_text=content,
        scene="general",
        context=None,
    )
    print(json.dumps(translated, ensure_ascii=False, indent=2))

    return translated["Data"]["Translated"]

def is_text_file(file_path: str) -> bool:
    """判断文件是否为文本文件"""
    text_extensions = {'.txt', '.py', '.md', '.java', '.c', '.cpp', '.h', '.html', '.css', '.js', '.json', '.xml'}
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in text_extensions:
        return False

    try:
        with open(file_path, 'rb') as f:
            raw_data = f.read(1024)
            if not raw_data:
                return True
            result = chardet.detect(raw_data)
            text_encodings = {'utf-8', 'gb2312', 'gbk', 'ascii', 'utf-16'}
            return result['encoding'] in text_encodings
    except:
        return False


def process_file(source_file: str, target_file: str):
    if is_text_file(source_file):
        print(f"处理文本文件（翻译）：{source_file} -> {target_file}")
        try:
            # 读取并检测编码
            with open(source_file, 'rb') as f:
                raw_data = f.read()
                encoding = chardet.detect(raw_data)['encoding'] or 'utf-8'
            with open(source_file, 'r', encoding=encoding, errors='ignore') as f:
                content = f.read()

            translated_content = translate_text(content)

            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(translated_content)
        except Exception as e:
            print(e)
            shutil.copy2(source_file, target_file)
    else:
        print(f"复制非文本文件：{source_file} -> {target_file}")
        try:
            shutil.copy2(source_file, target_file)
        except Exception as e:
            print(e)

def recursive_copy_and_translate(source_path: str, target_path: str):
    """
    :param source_path: 源文件/目录路径
    :param target_path: 目标文件/目录路径
    """
    if os.path.isfile(source_path):
        process_file(source_path, target_path)
        return

    if os.path.isdir(source_path):
        os.makedirs(target_path, exist_ok=True)

        for item in os.listdir(source_path):
            source_item = os.path.join(source_path, item)
            target_item = os.path.join(target_path, item)

            recursive_copy_and_translate(source_item, target_item)
        return

    print(f"源路径不存在，跳过：{source_path}")

# ====================== 测试用例 ======================
if __name__ == "__main__":
    SOURCE_DIR = "./doc-localizer"
    TARGET_DIR = "./tmp/proxyman-doc-zh"
    recursive_copy_and_translate(SOURCE_DIR, TARGET_DIR)
    print("ok.")