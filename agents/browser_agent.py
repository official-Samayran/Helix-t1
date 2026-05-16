from tools.browser_tool import BrowserTool


class BrowserAgent:

    @staticmethod
    def execute(prompt):

        p = prompt.lower()

        if "youtube" in p:
            return BrowserTool.open("https://youtube.com")

        if "google" in p:
            return BrowserTool.open("https://google.com")

        return "Unknown browser command"