from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import re
from collections import Counter

app = FastAPI()

def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        stopwords = file.read().splitlines()
    return stopwords

vietnamese_stopwords = load_stopwords('vietnamese-stopwords.txt')

def preprocess_text(text):
    # Tokenize
    tokens = re.findall(r'\b\w+\b', text.lower())
    # Loại bỏ stopwords
    filtered_tokens = [word for word in tokens if word not in vietnamese_stopwords]
    return filtered_tokens

class Texts(BaseModel):
    text1: str
    text2: str

@app.post("/process-text/")
async def process_text(texts: Texts):
    results = {}

    for i, text in enumerate([texts.text1, texts.text2], start=1):
        # Bước 1: Tokenize
        tokens = preprocess_text(text)

        # Bước 2: Tạo từ điển với tần suất
        dictionary = Counter(tokens)

        # Bước 3: Chuyển hóa thành vector TF-IDF
        tfidf_vectorizer = TfidfVectorizer(stop_words=vietnamese_stopwords)
        tfidf_matrix = tfidf_vectorizer.fit_transform([text])

        # Chọn vector cho văn bản
        vector = tfidf_matrix[0]

        # Kết quả cho từng đoạn văn bản
        results[f"text{i}"] = {
            "tokenize": tokens,
            "dictionary": {word: int(count) for word, count in dictionary.items()},
            "tfidf-vector": [(int(j), float(vector[0, j])) for j in vector.nonzero()[1]]
        }

    return results
