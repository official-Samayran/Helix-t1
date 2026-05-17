export default function TelemetryPanel() {

    return (

        <div
            style={{
                width: "100%",
                height: "90px",
                borderBottom: "1px solid #1f1f1f",
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                padding: "0 24px",
                background: "#050505"
            }}
        >

            <div
                style={{
                    display: "flex",
                    gap: "16px"
                }}
            >

                <div
                    style={{
                        width: "90px",
                        height: "70px",
                        border: "1px solid #1f1f1f",
                        borderRadius: "18px",
                        background: "#0d0d0d",
                        padding: "12px",
                        color: "white"
                    }}
                >
                    <div
                        style={{
                            color: "#888",
                            fontSize: "14px"
                        }}
                    >
                        CPU
                    </div>

                    <div
                        style={{
                            marginTop: "6px",
                            fontSize: "32px",
                            fontWeight: "700"
                        }}
                    >
                        7%
                    </div>
                </div>

                <div
                    style={{
                        width: "90px",
                        height: "70px",
                        border: "1px solid #1f1f1f",
                        borderRadius: "18px",
                        background: "#0d0d0d",
                        padding: "12px",
                        color: "white"
                    }}
                >
                    <div
                        style={{
                            color: "#888",
                            fontSize: "14px"
                        }}
                    >
                        RAM
                    </div>

                    <div
                        style={{
                            marginTop: "6px",
                            fontSize: "32px",
                            fontWeight: "700"
                        }}
                    >
                        42%
                    </div>
                </div>

            </div>

            <div
                style={{
                    display: "flex",
                    gap: "16px"
                }}
            >

                <div
                    style={{
                        border: "1px solid #1f1f1f",
                        borderRadius: "18px",
                        padding: "14px 18px",
                        background: "#0d0d0d",
                        color: "white"
                    }}
                >
                    <div>Llama 3.1</div>

                    <div
                        style={{
                            color: "#00ff88",
                            marginTop: "8px",
                            fontWeight: "700"
                        }}
                    >
                        ACTIVE
                    </div>
                </div>

                <div
                    style={{
                        border: "1px solid #1f1f1f",
                        borderRadius: "18px",
                        padding: "14px 18px",
                        background: "#0d0d0d",
                        color: "white"
                    }}
                >
                    <div>DeepSeek</div>

                    <div
                        style={{
                            color: "#00ff88",
                            marginTop: "8px",
                            fontWeight: "700"
                        }}
                    >
                        READY
                    </div>
                </div>

            </div>

        </div>
    );
}