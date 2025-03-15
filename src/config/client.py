from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv(override=True)

_openai_client = None

def get_openai_client() -> OpenAI:
    global _openai_client
    if _openai_client is None:
        openai_key = os.getenv("OPENAI_API_KEY")
        _openai_client = OpenAI(api_key='openai_key')
    return _openai_client