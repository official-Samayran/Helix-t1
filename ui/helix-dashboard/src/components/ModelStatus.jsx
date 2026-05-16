export default function ModelStatus() {

    return (
        <div
            style={{
                display: "flex",
                gap: 15
            }}
        >

            <div className="card">
                <h3>Llama 3.1</h3>
                <p className="status-online">
                    ACTIVE
                </p>
            </div>

            <div className="card">
                <h3>DeepSeek</h3>
                <p className="status-online">
                    READY
                </p>
            </div>

        </div>
    )
}