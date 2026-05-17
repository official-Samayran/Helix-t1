import { useEffect, useRef, useState } from "react"

import axios from "axios"

import ReactMarkdown from "react-markdown"

import remarkGfm from "remark-gfm"


export default function ChatPanel() {

    const [messages, setMessages] = useState([])

    const [input, setInput] = useState("")

    const wsRef = useRef(null)

    useEffect(() => {

        const ws = new WebSocket(
            "ws://127.0.0.1:8000/ws/events"
        )

        wsRef.current = ws

        ws.onmessage = (event) => {

            const data = JSON.parse(
                event.data
            )

            if (
                data.type === "token"
            ) {

                setMessages(prev => {

                    const updated = [...prev]

                    const last =
                        updated[
                            updated.length - 1
                        ]

                    if (
                        !last
                        ||
                        last.role !== "assistant"
                    ) {

                        updated.push({
                            role: "assistant",
                            content: data.token
                        })

                    } else {

                        last.content += data.token
                    }

                    return [...updated]
                })
            }

            if (
                data.type === "thinking"
            ) {

                setMessages(prev => [
                    ...prev,
                    {
                        role: "assistant",
                        content:
                            `*${data.message}*`
                    }
                ])
            }
        }

        ws.onerror = (err) => {

            console.error(
                "WebSocket Error",
                err
            )
        }

        return () => {

            ws.close()
        }

    }, [])

    async function sendMessage() {

        if (!input.trim()) return

        const userInput = input

        setMessages(prev => [
            ...prev,
            {
                role: "user",
                content: userInput
            }
        ])

        setInput("")

        try {

            await axios.post(
                "http://127.0.0.1:8000/chat",
                {
                    prompt: userInput
                }
            )

        } catch (error) {

            console.error(error)

            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    content:
                        "Backend crashed internally."
                }
            ])
        }
    }

    return (
        <>

            <div className="chat-container">

                {messages.map(
                    (msg, index) => (

                    <div
                        key={index}
                        className={`message ${msg.role}`}
                    >

                        <ReactMarkdown
                            remarkPlugins={[
                                remarkGfm
                            ]}
                        >
                            {msg.content}
                        </ReactMarkdown>

                    </div>
                ))}

            </div>

            <div className="input-bar">

                <input
                    value={input}
                    onChange={(e) => {

                        setInput(
                            e.target.value
                        )
                    }}
                    placeholder="Message HELIX..."
                    onKeyDown={(e) => {

                        if (
                            e.key === "Enter"
                        ) {

                            sendMessage()
                        }
                    }}
                />

                <button
                    onClick={sendMessage}
                >
                    Send
                </button>

            </div>

        </>
    )
}