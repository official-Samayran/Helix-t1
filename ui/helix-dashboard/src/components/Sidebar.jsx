const navItems = [
]

export default function Sidebar(){

    return(

        <aside
            style={{
                width:"260px",
                height:"100vh",
                padding:"24px",
                borderRight:"1px solid #1d1d1d",
                background:"#080808",
                display:"flex",
                flexDirection:"column",
                justifyContent:"space-between"
            }}
        >

            <div>

                <div
                    style={{
                        fontSize:"28px",
                        fontWeight:700,
                        letterSpacing:"10px",
                        marginBottom:"40px"
                    }}
                >
                    HELIX
                </div>

                <div
                    style={{
                        display:"flex",
                        flexDirection:"column",
                        gap:"10px"
                    }}
                >

                    {
                        navItems.map(item=>(

                            <button
                                key={item}
                                style={{
                                    width:"100%",
                                    background:"#101010",
                                    border:"1px solid #1d1d1d",
                                    color:"#f5f5f5",
                                    padding:"14px 16px",
                                    borderRadius:"16px",
                                    textAlign:"left",
                                    cursor:"pointer",
                                    transition:"0.2s"
                                }}
                            >
                                {item}
                            </button>
                        ))
                    }

                </div>

            </div>

            <div
                className="card"
                style={{
                    padding:"18px"
                }}
            >

                <div
                    className="muted"
                    style={{
                        fontSize:"14px"
                    }}
                >
                    SYSTEM STATUS
                </div>

                <div
                    style={{
                        marginTop:"10px",
                        display:"flex",
                        alignItems:"center",
                        gap:"10px"
                    }}
                >

                    <div
                        style={{
                            width:"10px",
                            height:"10px",
                            borderRadius:"999px",
                            background:"#7dffb3"
                        }}
                    />

                    <div
                        style={{
                            fontWeight:600
                        }}
                    >
                        ONLINE
                    </div>

                </div>

            </div>

        </aside>
    )
}