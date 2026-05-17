from agents.coding_agent import (
    CodingAgent
)

from agents.system_agent import (
    SystemAgent
)

from agents.browser_agent import (
    BrowserAgent
)

from agents.desktop_agent import (
    DesktopAgent
)

from agents.brain_agent import (
    BrainAgent
)

from core.router import (
    Router
)

from core.logger import (
    HelixLogger
)


class Orchestrator:

    logger = HelixLogger(
        "brain"
    )

    def process(
        self,
        prompt
    ):

        intent = Router.classify(
            prompt
        )

        self.logger.log(
            f"Intent => {intent}"
        )

        if intent == "coding":

            return CodingAgent.execute(
                prompt
            )

        elif intent == "system":

            return SystemAgent.execute(
                prompt
            )

        elif intent == "browser":

            return BrowserAgent.execute(
                prompt
            )

        elif intent == "desktop":

            return DesktopAgent.execute(
                prompt
            )

        else:

            return BrainAgent.execute(
                prompt
            )