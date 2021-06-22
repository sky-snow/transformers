from pathlib import Path
from transformers import BertTokenizer


def read_imdb_split(split_dir):
    split_dir = Path(split_dir)
    texts = []
    labels = []
    for label_dir in ["pos", "neg"]:
        for text_file in (split_dir / label_dir).iterdir():
            texts.append(text_file.read_text(encoding='utf-8'))
            labels.append(0 if label_dir is "neg" else 1)

    return texts, labels


train_texts, train_labels = read_imdb_split(r'I:\data\aclImdb_v1\aclImdb\train')
# test_texts, test_labels = read_imdb_split(r'I:\data\aclImdb_v1\aclImdb\test')
print(train_texts[:10])
print(train_labels[:10])
from sklearn.model_selection import train_test_split

# train_texts, val_texts, train_labels, val_labels = train_test_split(train_texts, train_labels, test_size=.2)


tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

train_encodings = tokenizer(train_texts, truncation=True, padding=True)
# val_encodings = tokenizer(val_texts, truncation=True, padding=True)
# test_encodings = tokenizer(test_texts, truncation=True, padding=True)
