import { useEffect, useState } from "react"

export default function TelemetryPanel() {

    const [stats, setStats] = useState({
        cpu: 0,
        ram: 0
    })

    useEffect(() => {

        const interval = setInterval(() => {

            setStats({
                cpu: Math.floor(Math.random() * 100),
                ram: Math.floor(Math.random() * 100)
            })

        }, 2000)

        return () => clearInterval(interval)

    }, [])

    return (
        <div
            style={{
                display: "flex",
                gap: 15
            }}
        >

            <div className="card">
                <h3>CPU</h3>
                <h1>{stats.cpu}%</h1>
            </div>

            <div className="card">
                <h3>RAM</h3>
                <h1>{stats.ram}%</h1>
            </div>

        </div>
    )
}