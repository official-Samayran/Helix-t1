from fastapi import FastAPI
from fastapi.middleware.cors import (
    CORSMiddleware
)

from fastapi import WebSocket

from pydantic import BaseModel

import traceback

from core.orchestrator import (
    Orchestrator
)

from api.events_ws import (
    EventsWS
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

orchestrator = Orchestrator()

events_ws = EventsWS()


class ChatRequest(BaseModel):

    prompt: str


@app.post("/chat")
def chat(req: ChatRequest):

    try:

        response = orchestrator.process(
            req.prompt
        )

        return {
            "success": True,
            "response": response
        }

    except Exception as e:

        traceback.print_exc()

        return {
            "success": False,
            "error": str(e)
        }


@app.websocket("/ws/events")
async def websocket_events(
    websocket: WebSocket
):

    await events_ws.handle(
        websocket
    )