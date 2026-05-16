from playwright.sync_api import sync_playwright


class BrowserTool:

    browser = None
    page = None
    playwright = None

    @staticmethod
    def start():
        BrowserTool.playwright = sync_playwright().start()

        BrowserTool.browser = BrowserTool.playwright.chromium.launch(
            headless=False
        )

        BrowserTool.page = BrowserTool.browser.new_page()

    @staticmethod
    def open(url):
        if BrowserTool.page is None:
            BrowserTool.start()

        BrowserTool.page.goto(url)

        return f"Opened {url}"

    @staticmethod
    def click(selector):
        BrowserTool.page.click(selector)

        return f"Clicked {selector}"

    @staticmethod
    def close():
        BrowserTool.browser.close()