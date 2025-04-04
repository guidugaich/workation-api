from dotenv import load_dotenv
import redis
import os

load_dotenv(override=True)

_cache_client = None

def get_cache_client() -> redis.Redis:
    global _cache_client
    if _cache_client is None:
        print('starting Redis instance')
        _cache_client = redis.Redis(
            host=os.getenv("REDIS_HOST"),
            port=os.getenv("REDIS_PORT"),
            decode_responses=True,
            username=os.getenv("REDIS_USERNAME"),
            password=os.getenv("REDIS_PASSWORD"),
        )
    return _cache_client