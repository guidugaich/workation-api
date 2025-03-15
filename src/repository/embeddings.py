from typing import List
from openai import OpenAI

class EmbeddingsRepository:
    def __init__(self, api: OpenAI):
        self.api = api

    def get_embeddings(self, query: str) -> List[float]:
        res = self.api.embeddings.create(
            model="text-embedding-3-small",
            input=query,
            encoding_format="float"
        )
        embedding = res.data[0].embedding
        print(f'embedded query "{query}" into a {len(list(embedding))} vector')
        return embedding