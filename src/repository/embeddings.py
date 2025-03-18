from typing import List
from openai import OpenAI

class EmbeddingsRepository:
    def __init__(self, api: OpenAI):
        self.api = api
        self.embedding_model_id = "text-embedding-3-small"

    def get_embeddings(self, query: str) -> List[float]:
        res = self.api.embeddings.create(
            model=self.embedding_model_id,
            input=query,
            encoding_format="float"
        )
        embedding = res.data[0].embedding
        print(f'embedded query "{query}" into a {len(list(embedding))} vector')
        return embedding