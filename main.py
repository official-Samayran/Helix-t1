import threading

import uvicorn
import pystray

from PIL import Image
from PIL import ImageDraw

from api.server import app


def create_tray():

    image = Image.new(
        "RGB",
        (64, 64),
        (0, 0, 0)
    )

    draw = ImageDraw.Draw(image)

    draw.rectangle(
        (16, 16, 48, 48),
        fill=(255, 255, 255)
    )

    tray = pystray.Icon(
        "HELIX",
        image,
        "HELIX ONLINE"
    )

    tray.run()


if __name__ == "__main__":

    threading.Thread(
        target=create_tray,
        daemon=True
    ).start()

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )