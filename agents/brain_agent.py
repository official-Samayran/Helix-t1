from models.ollama_client import (
    OllamaClient
)

from core.config import (
    MODELS
)

from core.event_bus import (
    EventBus
)


class BrainAgent:

    @staticmethod
    def execute(prompt):

        EventBus.emit({
            "type": "thinking",
            "message": "Thinking..."
        })

        response = (
            OllamaClient.stream_generate(
                MODELS["brain"],
                prompt,
                "assistant"
            )
        )

        return response