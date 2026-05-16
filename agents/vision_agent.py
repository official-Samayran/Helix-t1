from tools.screen_tool import (
    ScreenTool
)

from tools.ocr_tool import (
    OCRTool
)

from models.ollama_client import (
    OllamaClient
)

from core.config import MODELS


class VisionAgent:

    @staticmethod
    def analyze_screen():

        screenshot_path = (
            ScreenTool.capture()
        )

        extracted_text = (
            OCRTool.extract_text(
                screenshot_path
            )
        )

        prompt = f"""
You are a desktop vision agent.

SCREEN OCR:
{extracted_text}

TASK:
Describe what is happening on screen.
Identify apps/windows/buttons if possible.
"""

        analysis = OllamaClient.generate(
            MODELS["brain"],
            prompt
        )

        return {
            "screenshot": screenshot_path,
            "ocr_text": extracted_text,
            "analysis": analysis
        }