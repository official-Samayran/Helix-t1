const metrics = [

    {
        label:"CPU",
        value:"7%"
    },

    {
        label:"RAM",
        value:"42%"
    },

    {
        label:"GPU",
        value:"11%"
    }
]

export default function TelemetryPanel(){

    return(

        <div
            style={{
                height:"74px",
                borderBottom:"1px solid #1d1d1d",
                padding:"0 24px",
                display:"flex",
                justifyContent:"space-between",
                alignItems:"center",
                background:"#070707"
            }}
        >

            <div
                style={{
                    display:"flex",
                    gap:"14px"
                }}
            >

                {
                    metrics.map(metric=>(

                        <div
                            key={metric.label}
                            className="card"
                            style={{
                                padding:"10px 14px",
                                minWidth:"100px"
                            }}
                        >

                            <div
                                className="muted"
                                style={{
                                    fontSize:"12px"
                                }}
                            >
                                {metric.label}
                            </div>

                            <div
                                style={{
                                    marginTop:"4px",
                                    fontSize:"22px",
                                    fontWeight:700
                                }}
                            >
                                {metric.value}
                            </div>

                        </div>
                    ))
                }

            </div>

            <div
                style={{
                    display:"flex",
                    alignItems:"center",
                    gap:"14px"
                }}
            >

                <div className="muted">
                    Ollama Connected
                </div>

                <div
                    style={{
                        width:"10px",
                        height:"10px",
                        borderRadius:"999px",
                        background:"#7dffb3"
                    }}
                />

            </div>

        </div>
    )
}