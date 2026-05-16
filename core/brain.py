from models.ollama_client import OllamaClient
from core.config import MODELS


class Brain:

    SYSTEM_PROMPT = """
You are HELIX.
You are Samayran's AI operating system.
You are calm, intelligent, concise.
You supervise all agents.
"""

    @staticmethod
    def think(prompt):

        full_prompt = f"""
{Brain.SYSTEM_PROMPT}

USER:
{prompt}
"""

        return OllamaClient.generate(
            MODELS["brain"],
            full_prompt
        )