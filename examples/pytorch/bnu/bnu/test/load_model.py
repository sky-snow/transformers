from transformers import pipeline,  AutoTokenizer,AutoModelForSequenceClassification


model = AutoModelForSequenceClassification.from_pretrained(r"I:\BTU\results")
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)