import "./index.css";

import Sidebar from "./components/Sidebar";
import TelemetryPanel from "./components/TelemetryPanel";
import ChatPanel from "./components/ChatPanel";

export default function App() {

    return (

        <div className="app">

            <Sidebar />

            <div className="main">

                <TelemetryPanel />

                <ChatPanel />

            </div>

        </div>
    );
}