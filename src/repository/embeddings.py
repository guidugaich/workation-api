from typing import List
from openai import OpenAI
import redis
import json
from src.config.enum_helper import enum

class EmbeddingsRepository:
    def __init__(self, api: OpenAI, cache: redis.Redis):
        self.api = api
        self.cache = cache
        self.model_id = enum["embedding_model_id"]

    def get_embeddings(self, query: str) -> List[float]:
        res = self.api.embeddings.create(
            model=self.model_id,
            input=query,
            encoding_format="float"
        )
        embedding = res.data[0].embedding
        print(f'embedded query "{query}" into a {len(list(embedding))} vector')
        return embedding
    
    def get_embeddings_cache(self, query: str) -> List[float]:
        key = f"embeddings:{query}"
        cached_embedding = self.cache.get(key)
        if cached_embedding:
            print(f'found cached embeddings for "{query}"')
            # Deserialize the JSON string back into a Python list
            return json.loads(cached_embedding)
        else:
            print(f'no cached embeddings for "{query}", calling openAI API')
            embeddings = self.get_embeddings(query)
            # Serialize the list into a JSON string before storing it in Redis
            self.cache.set(key, json.dumps(embeddings))
            return embeddings