import {
    useEffect,
    useState
} from "react"

import useEvents from "../hooks/useEvents"

export default function LogsPanel() {

    const [logs, setLogs] =
        useState([])

    const event = useEvents()

    useEffect(() => {

        if (!event) return

        if (
            event.message
        ) {

            setLogs(prev => [

                ...prev,

                {
                    type:
                        event.type || "info",

                    message:
                        event.message,

                    time:
                        new Date()
                        .toLocaleTimeString()
                }
            ])
        }

    }, [event])

    return (

        <div className="terminal-panel">

            <div className="terminal-header">
                HELIX TERMINAL
            </div>

            <div className="terminal-body">

                {logs.map(
                    (log, index) => (

                    <div
                        key={index}
                        className={`terminal-line ${log.type}`}
                    >

                        <span className="terminal-time">
                            [{log.time}]
                        </span>

                        <span className="terminal-type">
                            {log.type}
                        </span>

                        <span className="terminal-message">
                            {log.message}
                        </span>

                    </div>
                ))}

            </div>

        </div>
    )
}