from pathlib import Path
from sklearn.model_selection import train_test_split


# root_path = r"/home/wuyan/usr/material/bert_corpus"
# path = [str(x) for x in Path(root_path).glob("**/*.txt")]


def merge_text(output_file, filenames):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        try:
            for names in filenames:
                with open(names, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n')
                    print(names + ' has been process')
        except UnicodeDecodeError as e:
            print('except', e)
            print(names)
            # outfile.write("\n")


if __name__ == '__main__':
    # root_path = r"I:\\BTU\\annotation\\"
    root_path = r"I:\\BTU\\data\\language_model_corpus\\"
    # root_path = r"I:\BTU\data\language_model_corpus\matrial_corpus\alloys\1"
    path = [str(x) for x in Path(root_path).glob("**/*.txt")]
    print(len(path))
    train_texts, val_texts = train_test_split(path, test_size=.2)
    print(len(train_texts))
    print("\n")
    print(len(val_texts))
    merge_text("train.txt", train_texts)
    merge_text("validation.txt", val_texts)
