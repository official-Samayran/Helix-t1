import {
    useEffect,
    useState
} from "react"

let socket = null

export default function useEvents() {

    const [event, setEvent] =
        useState(null)

    useEffect(() => {

        if (!socket) {

            socket = new WebSocket(
                "ws://127.0.0.1:8000/ws/events"
            )
        }

        socket.onmessage = (e) => {

            const data = JSON.parse(
                e.data
            )

            setEvent(data)
        }

    }, [])

    return event
}