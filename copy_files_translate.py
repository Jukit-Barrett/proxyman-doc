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

# ====================== 辅助函数 ======================
def is_text_file(file_path: str) -> bool:
    """判断文件是否为文本文件（后缀+编码检测）"""
    text_extensions = {'.txt', '.py', '.md', '.java', '.c', '.cpp', '.h', '.html', '.css', '.js', '.json', '.xml'}
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in text_extensions:
        return False

    # 编码检测确认
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
    """处理单个文件：文本文件翻译，非文本文件直接复制"""
    if is_text_file(source_file):
        print(f"处理文本文件（翻译）：{source_file} -> {target_file}")
        try:
            # 读取并检测编码
            with open(source_file, 'rb') as f:
                raw_data = f.read()
                encoding = chardet.detect(raw_data)['encoding'] or 'utf-8'
            with open(source_file, 'r', encoding=encoding, errors='ignore') as f:
                content = f.read()

            # 调用翻译钩子
            translated_content = translate_text(content)

            # 写入目标文件
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(translated_content)
        except Exception as e:
            print(f"文本文件处理失败，直接复制原文件：{source_file}，错误：{str(e)}")
            shutil.copy2(source_file, target_file)
    else:
        print(f"复制非文本文件：{source_file} -> {target_file}")
        try:
            shutil.copy2(source_file, target_file)
        except Exception as e:
            print(f"非文本文件复制失败：{source_file}，错误：{str(e)}")


# ====================== 核心递归函数（真正的递归实现） ======================
def recursive_copy_and_translate(source_path: str, target_path: str):
    """
    显式递归实现：递归复制目录/文件，文本文件翻译后保存
    :param source_path: 源文件/目录路径
    :param target_path: 目标文件/目录路径
    """
    # 1. 如果源路径是文件：直接处理
    if os.path.isfile(source_path):
        process_file(source_path, target_path)
        return

    # 2. 如果源路径是目录：创建目标目录，递归处理子项
    if os.path.isdir(source_path):
        # 创建目标目录（不存在则创建）
        os.makedirs(target_path, exist_ok=True)

        # 遍历当前目录下的所有子项（文件/子目录）
        for item in os.listdir(source_path):
            source_item = os.path.join(source_path, item)
            target_item = os.path.join(target_path, item)

            # 递归调用自身，处理子项
            recursive_copy_and_translate(source_item, target_item)
        return

    # 3. 源路径不存在
    print(f"源路径不存在，跳过：{source_path}")

# ====================== 测试用例 ======================
if __name__ == "__main__":
    SOURCE_DIR = "./doc-localizer"
    TARGET_DIR = "./tmp/proxyman-doc-zh"
    recursive_copy_and_translate(SOURCE_DIR, TARGET_DIR)
    print("复制/翻译完成！")