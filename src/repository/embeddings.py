from typing import List
from openai import OpenAI

class EmbeddingsRepository:
    def __init__(self, api: OpenAI):
        self.api = api

    def get_embeddings(self, query: str) -> List[float]:
        print('will call openai api', query)
        return []