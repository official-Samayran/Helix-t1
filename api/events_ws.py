import asyncio

from fastapi import (
    WebSocket,
    WebSocketDisconnect
)

from core.event_bus import (
    EventBus
)


class EventsWS:

    async def handle(
        self,
        websocket: WebSocket
    ):

        await websocket.accept()

        queue = asyncio.Queue()

        def listener(event):

            try:

                queue.put_nowait(event)

            except:

                pass

        EventBus.subscribe(listener)

        try:

            while True:

                event = await queue.get()

                await websocket.send_json(
                    event
                )

        except WebSocketDisconnect:

            print(
                "WebSocket disconnected"
            )

        except Exception as e:

            print(
                f"WS ERROR: {e}"
            )