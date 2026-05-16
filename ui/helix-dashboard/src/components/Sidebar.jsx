export default function Sidebar() {

    return (
        <div className="sidebar">

            <h1
                style={{
                    marginBottom: 30,
                    fontSize: 28
                }}
            >
                H E L I X
            </h1>

            <div className="card">
                <h3>System</h3>
                <p className="status-online">
                    ONLINE
                </p>
            </div>

            <div className="card">
                <h3>Workspace</h3>
                <p>E:\\Helix_Projects</p>
            </div>

            <div className="card">
                <h3>Connection</h3>
                <p className="status-online">
                    Phone Connected
                </p>
            </div>

        </div>
    )
}