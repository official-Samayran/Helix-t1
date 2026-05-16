from fastapi import FastAPI
from fastapi.middleware.cors import (
    CORSMiddleware
)

from fastapi import WebSocket
from pydantic import BaseModel

from core.orchestrator import (
    Orchestrator
)

from api.live_terminal_ws import (
    LiveTerminalWS
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

live_terminal = LiveTerminalWS()

events_ws = EventsWS()


class ChatRequest(BaseModel):

    prompt: str


@app.post("/chat")
def chat(req: ChatRequest):

    response = orchestrator.process(
        req.prompt
    )

    return {
        "response": response
    }


@app.websocket("/ws/terminal")
async def websocket_terminal(
    websocket: WebSocket
):

    await live_terminal.handle(
        websocket
    )


@app.websocket("/ws/events")
async def websocket_events(
    websocket: WebSocket
):

    await events_ws.handle(
        websocket
    )