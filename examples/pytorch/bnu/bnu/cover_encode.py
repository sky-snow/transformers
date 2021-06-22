# -*- coding: utf-8 -*-
"""
# @ProjectName : transformers_bnu
# @FileName : cover_encode.py
# @Author :wuyan
# @time : 2021/5/19 22:19 2021
# @contact: skysnow2017@gmail.com
# @desc :
"""

from pathlib import Path
from chardet.universaldetector import UniversalDetector
import os

detector = UniversalDetector()


def convert_file_to_utf8(filename):
    detector.reset()
    for line in open(filename, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    file_encoding = detector.result['encoding']
    if file_encoding == 'utf-8':
        # print(detector.result['encoding'], '\t', filename)
        pass
    elif file_encoding is None:
        os.remove(filename)
    elif file_encoding == 'ascii':
        print(file_encoding)
        f = open(filename, 'r', encoding=file_encoding, errors='replace')
        text = f.read()
        text = text.encode('utf-8').decode('utf-8')
        f = open(filename, 'w', encoding='utf-8', errors='replace')
        f.write(text)
    else:
        f = open(filename, 'r', encoding=file_encoding, errors='replace')
        text = f.read()
        f = open(filename, 'w', encoding='utf-8', errors='replace')
        f.write(text)
        print(detector.result['encoding'], '\t', filename)


if __name__ == '__main__':
    # root_path = r"I:\\BTU\\annotation\\"
    root_path = r"I:\\BTU\\data\\language_model_corpus\\"
    # root_path = r"I:\BTU\data\language_model_corpus\matrial_corpus\alloys\1"
    paths = [str(x) for x in Path(root_path).glob("**/*.txt")]
    for path in paths:
        convert_file_to_utf8(path)
