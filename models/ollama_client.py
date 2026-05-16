import requests
from core.config import OLLAMA_URL


class OllamaClient:
    @staticmethod
    def generate(model, prompt):
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(OLLAMA_URL, json=payload)
        data = response.json()

        return data.get("response", "")