import Sidebar from "./components/Sidebar"
import ChatPanel from "./components/ChatPanel"
import TelemetryPanel from "./components/TelemetryPanel"
import ModelStatus from "./components/ModelStatus"
import LogsPanel from "./components/LogsPanel"

export default function App() {

    return (
        <div className="app">

            <Sidebar />

            <div className="main">

                <div className="topbar">

                    <TelemetryPanel />

                    <ModelStatus />

                </div>

                <ChatPanel />

                <LogsPanel />

            </div>

        </div>
    )
}