# -*- coding: utf-8 -*-
"""
# @ProjectName : transformers_bnu
# @FileName : test.py
# @Author :wuyan
# @time : 2021/5/12 20:03 2021
# @contact: skysnow2017@gmail.com
# @desc :
"""
from chardet import UniversalDetector
import pathlib
import chardet

detector = UniversalDetector()


def convert_file_to_utf8(filename):
    content = ""
    with open(filename, "rb") as f:
        content = f.read()
        if len(content) == 0:
            print(filename)
    source_encoding = chardet.detect(content)['encoding']
    if source_encoding is None:
        print("??", filename)
        return
    if source_encoding != 'utf-8':
        print("  ", source_encoding, filename)
        # content = content.decode(source_encoding, 'ignore')  # .encode(source_encoding)


if __name__ == '__main__':
    # root_path = r"I:\\BTU\\annotation\\"
    # root_path = r"I:\\BTU\\data\\language_model_corpus\\"
    root_path = r"I:\BTU\data\language_model_corpus\matrial_corpus\alloys\1"
    paths = [str(x) for x in pathlib.Path(root_path).glob("**/*.txt")]
    for path in paths:
        convert_file_to_utf8(path)
