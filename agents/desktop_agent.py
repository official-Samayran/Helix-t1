from tools.desktop_tool import (
    DesktopTool
)

from agents.vision_agent import (
    VisionAgent
)

from tools.windows_tool import (
    WindowsTool
)


class DesktopAgent:

    @staticmethod
    def execute(prompt):

        p = prompt.lower()

        if "open chrome" in p:

            WindowsTool.open_app(
                "chrome"
            )

            return "Chrome opened"

        if "analyze screen" in p:

            return VisionAgent.analyze_screen()

        if "search youtube" in p:

            WindowsTool.open_app(
                "chrome"
            )

            DesktopTool.wait(2)

            DesktopTool.hotkey(
                "ctrl",
                "l"
            )

            DesktopTool.type_text(
                "https://youtube.com"
            )

            DesktopTool.press("enter")

            return "YouTube opened"

        return "Unknown desktop command"