import time
import pyautogui


class DesktopTool:

    @staticmethod
    def click(
        x,
        y
    ):

        pyautogui.click(x, y)

        return f"Clicked {x}, {y}"

    @staticmethod
    def double_click(
        x,
        y
    ):

        pyautogui.doubleClick(x, y)

        return f"Double clicked {x}, {y}"

    @staticmethod
    def move_mouse(
        x,
        y,
        duration=0.2
    ):

        pyautogui.moveTo(
            x,
            y,
            duration=duration
        )

    @staticmethod
    def type_text(text):

        pyautogui.write(
            text,
            interval=0.02
        )

    @staticmethod
    def press(key):

        pyautogui.press(key)

    @staticmethod
    def hotkey(*keys):

        pyautogui.hotkey(*keys)

    @staticmethod
    def scroll(amount):

        pyautogui.scroll(amount)

    @staticmethod
    def wait(seconds):

        time.sleep(seconds)