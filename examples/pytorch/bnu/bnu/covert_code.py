# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 19:37
# @Author  : wuyan
# @Email   :aerolandX@163.com
# @FileName: covert_code.py
# @Function:


import chardet
import codecs
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count
from pathlib import Path


def get_encode_info(file):
    with open(file, 'rb') as f:
        file_encoding = chardet.detect(f.read())['encoding']
        return file_encoding


def read_file(file):
    with open(file, 'rb') as f:
        return f.read()


def write_file(content, file):
    with open(file, 'wb', encoding='utf-8') as f:
        f.write(content)


def convert_encode2utf8(file, original_encode, des_encode):
    file_content = read_file(file)
    if original_encode == None:
        original_encode = 'utf-8'
    file_decode = file_content.encode().decode(original_encode, 'ignore')
    file_content = file_decode.encode(des_encode)
    write_file(file_content, file)


def covert_all(file_path):
    encode_info = get_encode_info(file_path)
    if encode_info != 'utf-8':
        convert_encode2utf8(file_path, encode_info, 'utf-8')
        return file_path


def merge_text(filenames):
    with open('result.txt', 'w') as outfile:
        for names in filenames:
            with open(names, encoding='utf-8') as infile:
                outfile.write(infile.read())
            outfile.write("\n")


def multip_process(task: list):
    executor = ThreadPoolExecutor(max_workers=cpu_count())
    for result in executor.map(covert_all, task):
        print(result + ' has been processed')


if __name__ == '__main__':
    # root_path = r"I:\\BTU\\annotation\\"
    # root_path = r"I:\\BTU\\data\\language_model_corpus\\"
    root_path = r"I:\BTU\data\language_model_corpus\matrial_corpus\alloys\1"
    paths = [str(x) for x in Path(root_path).glob("**/*.txt")]
    # print(paths)
    # multip_process(paths)
    for path in paths:
        covert_all(path)
        # get_encode_info(path)
