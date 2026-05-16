from models.ollama_client import (
    OllamaClient
)

from core.config import MODELS


class FileGenerationAgent:

    @staticmethod
    def clean_code(text):

        text = text.strip()

        text = text.replace(
            "```python",
            ""
        )

        text = text.replace(
            "```",
            ""
        )

        return text.strip()

    @staticmethod
    def generate_file(
        project_prompt,
        project_plan,
        current_file,
        existing_files
    ):

        generation_prompt = f"""
You are an elite software engineer.

PROJECT REQUEST:
{project_prompt}

PROJECT PLAN:
{project_plan}

CURRENT FILE:
{current_file}

ALREADY GENERATED FILES:
{existing_files}

STRICT RULES:
1. Return ONLY raw code.
2. No markdown.
3. No explanations.
4. No comments outside code.
5. Generate COMPLETE file contents.
6. Code MUST run correctly.
7. Never explain anything.
"""

        response = OllamaClient.generate(
            MODELS["coder"],
            generation_prompt
        )

        return FileGenerationAgent.clean_code(
            response
        )