import pytesseract

from tools.screen_tool import (
    ScreenTool
)


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


class OCRTool:

    @staticmethod
    def extract_text(image_path):

        image = ScreenTool.load_image(
            image_path
        )

        gray = ScreenTool.grayscale(
            image
        )

        threshold = ScreenTool.threshold(
            gray
        )

        text = pytesseract.image_to_string(
            threshold
        )

        return text