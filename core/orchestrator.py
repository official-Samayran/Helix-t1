from core.router import Router

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

from core.brain import Brain
from core.memory import Memory
from core.logger import HelixLogger

WORKSPACE = r"E:\Helix_Projects"


class Orchestrator:

    def __init__(self):

        self.memory = Memory()

        self.logger = HelixLogger(
            "brain"
        )

        self.coding_agent = (
            CodingAgent()
        )

    def process(self, prompt):

        self.memory.save_message(
            "user",
            prompt
        )

        intent = Router.classify(
            prompt
        )

        self.logger.log(
            f"Intent => {intent}"
        )

        if intent == "coding":

            response = (
                self.coding_agent.execute(
                    prompt,
                    WORKSPACE
                )
            )

        elif intent == "system":

            response = (
                SystemAgent.execute(
                    prompt
                )
            )

        elif intent == "browser":

            response = (
                BrowserAgent.execute(
                    prompt
                )
            )

        elif intent == "desktop":

            response = (
                DesktopAgent.execute(
                    prompt
                )
            )

        else:

            response = Brain.think(
                prompt
            )

        self.memory.save_message(
            "assistant",
            str(response)
        )

        return response