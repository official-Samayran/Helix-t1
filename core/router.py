class Router:

    @staticmethod
    def classify(prompt: str):

        p = prompt.lower()

        coding_keywords = [
            "code",
            "python",
            "flutter",
            "build",
            "create",
            "generate",
            "debug",
            "program"
        ]

        system_keywords = [
            "wifi",
            "bluetooth",
            "shutdown",
            "restart",
            "volume",
            "brightness",
            "open chrome",
            "open app"
        ]

        browser_keywords = [
            "browser",
            "google",
            "youtube",
            "website"
        ]

        desktop_keywords = [
            "screen",
            "desktop",
            "click",
            "type",
            "mouse",
            "keyboard",
            "analyze screen"
        ]

        if any(
            k in p
            for k in coding_keywords
        ):
            return "coding"

        if any(
            k in p
            for k in system_keywords
        ):
            return "system"

        if any(
            k in p
            for k in browser_keywords
        ):
            return "browser"

        if any(
            k in p
            for k in desktop_keywords
        ):
            return "desktop"

        return "brain"