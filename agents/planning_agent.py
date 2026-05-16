import json
import re

from models.ollama_client import (
    OllamaClient
)

from core.config import MODELS


class PlanningAgent:

    @staticmethod
    def extract_json(text):

        start = text.find("{")

        end = text.rfind("}")

        if start == -1 or end == -1:
            return None

        return text[start:end + 1]

    @staticmethod
    def fallback_plan():

        return {
            "project_name": "calculator_app",
            "project_type": "python",
            "run_command": "python main.py",
            "dependencies": [],
            "files": [
                {
                    "path": "main.py",
                    "description": "Main application"
                }
            ]
        }

    @staticmethod
    def create_plan(prompt):

        planning_prompt = f"""
Generate ONLY valid JSON.

No explanations.
No markdown.
No comments.
No extra text.

TASK:
{prompt}

JSON FORMAT:
{{
    "project_name": "calculator_app",
    "project_type": "python",
    "run_command": "python main.py",
    "dependencies": [],
    "files": [
        {{
            "path": "main.py",
            "description": "Main application"
        }}
    ]
}}
"""

        response = OllamaClient.generate(
            MODELS["coder"],
            planning_prompt
        )

        print("\\nRAW RESPONSE:\\n")
        print(response)

        if not response:
            return PlanningAgent.fallback_plan()

        response = response.strip()

        response = response.replace(
            "```json",
            ""
        )

        response = response.replace(
            "```",
            ""
        )

        extracted_json = (
            PlanningAgent.extract_json(
                response
            )
        )

        if not extracted_json:

            print(
                "JSON EXTRACTION FAILED"
            )

            return PlanningAgent.fallback_plan()

        try:

            parsed = json.loads(
                extracted_json
            )

            if "project_name" not in parsed:
                return PlanningAgent.fallback_plan()

            return parsed

        except Exception as e:

            print(
                f"JSON ERROR: {e}"
            )

            return PlanningAgent.fallback_plan()