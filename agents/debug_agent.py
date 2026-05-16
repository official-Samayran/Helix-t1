import json
import re

from models.ollama_client import (
    OllamaClient
)

from core.config import MODELS


class DebugAgent:

    @staticmethod
    def extract_json(text):

        match = re.search(
            r"\{.*\}",
            text,
            re.DOTALL
        )

        if match:
            return match.group(0)

        return None

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
    def analyze_error(
        project_prompt,
        project_plan,
        generated_files,
        error_output
    ):

        debug_prompt = f"""
You are a senior debugging engineer.

PROJECT:
{project_prompt}

ERROR:
{error_output}

FILES:
{list(generated_files.keys())}

Return ONLY JSON.

FORMAT:
{{
    "broken_file": "main.py",
    "reason": "syntax error",
    "fix_strategy": "rewrite function"
}}
"""

        response = OllamaClient.generate(
            MODELS["coder"],
            debug_prompt
        )

        response = response.strip()

        response = response.replace(
            "```json",
            ""
        )

        response = response.replace(
            "```",
            ""
        )

        extracted = DebugAgent.extract_json(
            response
        )

        if not extracted:

            return {
                "broken_file": list(
                    generated_files.keys()
                )[0],
                "reason": "unknown",
                "fix_strategy": "rewrite file"
            }

        try:

            return json.loads(extracted)

        except:

            return {
                "broken_file": list(
                    generated_files.keys()
                )[0],
                "reason": "unknown",
                "fix_strategy": "rewrite file"
            }

    @staticmethod
    def fix_file(
        project_prompt,
        broken_file_path,
        broken_file_code,
        error_output,
        fix_strategy
    ):

        fix_prompt = f"""
Fix this broken code.

BROKEN FILE:
{broken_file_path}

CODE:
{broken_file_code}

ERROR:
{error_output}

FIX STRATEGY:
{fix_strategy}

STRICT RULES:
1. Return ONLY corrected raw code.
2. No markdown.
3. No explanations.
4. Return COMPLETE file.
5. Ensure code runs successfully.
"""

        response = OllamaClient.generate(
            MODELS["coder"],
            fix_prompt
        )

        return DebugAgent.clean_code(
            response
        )