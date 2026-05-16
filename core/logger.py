import os
from datetime import datetime

from core.event_bus import (
    EventBus
)


class HelixLogger:

    def __init__(self, category):

        self.category = category

        self.log_dir = os.path.join(
            "logs",
            category
        )

        os.makedirs(
            self.log_dir,
            exist_ok=True
        )

    def log(self, message):

        timestamp = datetime.now()

        filename = (
            f"{timestamp.date()}.log"
        )

        filepath = os.path.join(
            self.log_dir,
            filename
        )

        log_line = (
            f"[{timestamp}] {message}\n"
        )

        with open(
            filepath,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(log_line)

        print(log_line)

        EventBus.emit({
            "type": "log",
            "category": self.category,
            "message": message,
            "timestamp": str(timestamp)
        })