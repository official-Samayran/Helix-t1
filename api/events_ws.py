import asyncio

from fastapi import WebSocket

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

            queue.put_nowait(event)

        EventBus.subscribe(listener)

        while True:

            event = await queue.get()

            await websocket.send_json(
                event
            )