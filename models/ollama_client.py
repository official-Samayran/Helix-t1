import json
import requests

from core.event_bus import (
    EventBus
)


class OllamaClient:

    BASE_URL = (
        "http://localhost:11434/api/generate"
    )

    @staticmethod
    def generate(
        model,
        prompt
    ):

        response = requests.post(

            OllamaClient.BASE_URL,

            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        return data.get(
            "response",
            ""
        )

    @staticmethod
    def stream_generate(
        model,
        prompt,
        stream_type="assistant"
    ):

        response = requests.post(

            OllamaClient.BASE_URL,

            json={
                "model": model,
                "prompt": prompt,
                "stream": True
            },

            stream=True
        )

        full_text = ""

        for line in response.iter_lines():

            if not line:
                continue

            try:

                chunk = json.loads(
                    line.decode("utf-8")
                )

                token = chunk.get(
                    "response",
                    ""
                )

                if token:

                    full_text += token

                    EventBus.emit({
                        "type": "token",
                        "stream_type": stream_type,
                        "content": full_text
                    })

            except:
                pass

        return full_text