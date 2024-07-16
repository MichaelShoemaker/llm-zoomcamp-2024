## Q1
```
model_name='multi-qa-distilbert-cos-v1'
from sentence_transformers import SentenceTransformer
embedding_model = SentenceTransformer(model_name)

user_question = "I just discovered the course. Can I still join it?"

[0]
```


## Q2
```
documents = [x for x in documents if x['course']=='machine-learning-zoomcamp']
```

## Q3
```
import numpy as np
v = embedding_model.encode(user_question)
X = np.array(embeddings)
print(X.dot(v))
```

## Q4
```
class VectorSearchEngine():
    def __init__(self, documents, embeddings):
        self.documents = documents
        self.embeddings = embeddings

    def search(self, v_query, num_results=10):
        scores = self.embeddings.dot(v_query)
        idx = np.argsort(-scores)[:num_results]
        return [self.documents[i] for i in idx]

search_engine = VectorSearchEngine(documents=documents, embeddings=X)
results = search_engine.search(v, num_results=5)

def calculate_hit_rate(search_engine, ground_truth, num_results=5):
    hits = 0
    for item in ground_truth:
        query = item['question']
        expected_document_id = item['document']
        query_embedding = embedding_model.encode(query)
        results = search_engine.search(query_embedding, num_results)
        retrieved_ids = [doc['id'] for doc in results]
        if expected_document_id in retrieved_ids:
            hits += 1
    return hits / len(ground_truth)

hit_rate = calculate_hit_rate(search_engine, ground_truth, num_results=5)
print(hit_rate)
```

