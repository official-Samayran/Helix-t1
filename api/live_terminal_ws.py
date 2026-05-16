from fastapi import WebSocket

from tools.live_terminal_tool import (
    LiveTerminalTool
)


class LiveTerminalWS:

    async def handle(
        self,
        websocket: WebSocket
    ):

        await websocket.accept()

        while True:

            command = (
                await websocket.receive_text()
            )

            for line in (
                LiveTerminalTool.stream(command)
            ):

                await websocket.send_text(
                    line
                )