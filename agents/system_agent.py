from tools.windows_tool import (
    WindowsTool
)


class SystemAgent:

    @staticmethod
    def execute(prompt):

        p = prompt.lower()

        if "wifi off" in p:
            return WindowsTool.wifi_off()

        if "wifi on" in p:
            return WindowsTool.wifi_on()

        if "shutdown" in p:
            return WindowsTool.shutdown_pc()

        if "restart" in p:
            return WindowsTool.restart_pc()

        if "open chrome" in p:
            return WindowsTool.open_app(
                "chrome"
            )

        return "Unknown system command"