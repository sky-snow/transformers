# -*- coding: utf-8 -*-
"""
# @ProjectName : transformers_bnu
# @FileName : devide_sentence.py
# @Author :wuyan
# @time : 2021/5/30 15:49 2021
# @contact: skysnow2017@gmail.com
# @desc :
"""

from nltk.tokenize import sent_tokenize

if __name__ == '__main__':
    path = r'I:\BTU\data\language_model_corpus\bert_corpus\alloys\1\1.txt'
    # path = r'I:\BTU\data\row_corpus\train.txt'
    # path = r'I:\BTU\data\row_corpus\validation.txt'
    with open(path, 'r+', encoding='utf-8') as f:
        text = f.read()
        sentence_text = sent_tokenize(text)
        f.seek(0)
        f.truncate()
        for line in sentence_text:
            # print(len(line), '\t')
            f.writelines(line)
            f.write('\n')
