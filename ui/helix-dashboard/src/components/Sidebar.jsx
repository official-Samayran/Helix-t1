export default function Sidebar() {

    return (

        <div
            style={{
                width: "260px",
                height: "100vh",
                background: "#0b0b0b",
                borderRight: "1px solid #1f1f1f",
                padding: "24px",
                color: "white"
            }}
        >

            <div
                style={{
                    fontSize: "38px",
                    fontWeight: "700",
                    letterSpacing: "12px",
                    marginBottom: "40px"
                }}
            >
                HELIX
            </div>

            <div
                style={{
                    border: "1px solid #1f1f1f",
                    borderRadius: "18px",
                    padding: "20px",
                    marginBottom: "20px",
                    background: "#111"
                }}
            >
                <div style={{ color: "#777" }}>
                    System
                </div>

                <div
                    style={{
                        color: "#00ff88",
                        marginTop: "8px",
                        fontWeight: "600"
                    }}
                >
                    ONLINE
                </div>
            </div>

        </div>
    );
}