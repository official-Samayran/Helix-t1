import { useEffect, useState } from "react"

export default function LogsPanel() {

    const [events, setEvents] = useState([])

    useEffect(() => {

        const ws = new WebSocket(
            "ws://127.0.0.1:8000/ws/events"
        )

        ws.onmessage = (event) => {

            const data = JSON.parse(
                event.data
            )

            setEvents(prev => [
                data,
                ...prev.slice(0, 100)
            ])
        }

        return () => ws.close()

    }, [])

    return (

        <div className="logs-panel">

            <h3
                style={{
                    marginBottom: 15
                }}
            >
                Agent Activity
            </h3>

            {events.map(
                (event, index) => (

                <div
                    key={index}
                    style={{
                        marginBottom: 12,
                        padding: 12,
                        borderRadius: 12,
                        background: "#111"
                    }}
                >

                    <div
                        style={{
                            color: "#4ade80",
                            fontSize: 12,
                            marginBottom: 5
                        }}
                    >
                        {event.type}
                    </div>

                    <div
                        style={{
                            fontSize: 14,
                            color: "white"
                        }}
                    >
                        {
                            event.message
                            ||
                            event.token
                        }
                    </div>

                </div>
            ))}

        </div>
    )
}