import {
    useEffect,
    useState
} from "react"

export default function LogsPanel() {

    const [logs, setLogs] =
        useState([])

    useEffect(() => {

        const event = useEvents()

        ws.onmessage = (event) => {

            const data = JSON.parse(
                event.data
            )

            if (
                data.message
            ) {

                setLogs(prev => [

                    ...prev,

                    {
                        type:
                            data.type,

                        message:
                            data.message
                    }
                ])
            }
        }

        return () => ws.close()

    }, [])

    return (

        <div className={`terminal-line ${log.type}`}>

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
                            [
                            {
                                new Date()
                                .toLocaleTimeString()
                            }
                            ]
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