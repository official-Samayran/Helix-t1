import "./index.css";

import Sidebar from "./components/Sidebar";
import TelemetryPanel from "./components/TelemetryPanel";
import ChatPanel from "./components/ChatPanel";

export default function App() {

    return (

        <div className="layout">

            <Sidebar />

            <main className="workspace">

                <TelemetryPanel />

                <ChatPanel />

            </main>

        </div>
    );
}