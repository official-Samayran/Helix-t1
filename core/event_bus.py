class EventBus:

    listeners = []

    @staticmethod
    def subscribe(callback):

        EventBus.listeners.append(
            callback
        )

    @staticmethod
    def emit(event):

        for listener in (
            EventBus.listeners
        ):

            listener(event)