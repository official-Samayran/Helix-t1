import os
import time

import cv2
import mss
import numpy as np

from PIL import Image


class ScreenTool:

    SCREENSHOT_DIR = r"E:\Helix\screenshots"

    @staticmethod
    def ensure_dir():

        os.makedirs(
            ScreenTool.SCREENSHOT_DIR,
            exist_ok=True
        )

    @staticmethod
    def capture():

        ScreenTool.ensure_dir()

        timestamp = int(time.time())

        path = os.path.join(
            ScreenTool.SCREENSHOT_DIR,
            f"{timestamp}.png"
        )

        with mss.mss() as sct:

            monitor = sct.monitors[1]

            screenshot = sct.grab(monitor)

            img = Image.frombytes(
                "RGB",
                screenshot.size,
                screenshot.rgb
            )

            img.save(path)

        return path

    @staticmethod
    def load_image(path):

        return cv2.imread(path)

    @staticmethod
    def resize(
        image,
        scale=0.5
    ):

        width = int(
            image.shape[1] * scale
        )

        height = int(
            image.shape[0] * scale
        )

        return cv2.resize(
            image,
            (width, height)
        )

    @staticmethod
    def grayscale(image):

        return cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

    @staticmethod
    def threshold(image):

        return cv2.threshold(
            image,
            150,
            255,
            cv2.THRESH_BINARY
        )[1]