import {
    useEffect,
    useRef,
    useState
} from "react"

import useEvents from "../hooks/useEvents"

import axios from "axios"

import ReactMarkdown from "react-markdown"

import remarkGfm from "remark-gfm"

export default function ChatPanel() {

    const [messages, setMessages] =
        useState([])

    const [input, setInput] =
        useState("")

    const messagesEndRef =
        useRef(null)

    useEffect(() => {

        messagesEndRef.current?.
        scrollIntoView({
            behavior: "smooth"
        })

    }, [messages])

    useEffect(() => {

        const event = useEvents()

        ws.onmessage = (event) => {

            const data = JSON.parse(
                event.data
            )

            if (
                data.type === "thinking"
            ) {

                setMessages(prev => [

                    ...prev,

                    {
                        role: "assistant",
                        content: "Thinking..."
                    }
                ])
            }

            if (
                data.type === "token"
            ) {

                setMessages(prev => {

                    const updated = [
                        ...prev
                    ]

                    const last =
                        updated[
                            updated.length - 1
                        ]

                    if (
                        last &&
                        last.role === "assistant"
                    ) {

                        last.content =
                            data.content

                    } else {

                        updated.push({

                            role: "assistant",

                            content:
                                data.content
                        })
                    }

                    return [...updated]
                })
            }
        }

        return () => ws.close()

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

        } catch {

            setMessages(prev => [

                ...prev,

                {
                    role: "assistant",
                    content:
                        "Backend error."
                }
            ])
        }
    }

    return (

        <div className="chat-wrapper">

            <div className="chat-container">

                {messages.map(
                    (msg, index) => (

                    <div
                        key={index}
                        className={`message-row ${msg.role}`}
                    >

                        {
                            msg.role ===
                            "assistant" && (

                                <div className="avatar">
                                    H
                                </div>
                            )
                        }

                        <div
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

                    </div>
                ))}

                <div ref={messagesEndRef} />

            </div>

            <div className="input-container">

                <div className="input-bar">

                    <input
                        value={input}
                        onChange={(e) =>
                            setInput(
                                e.target.value
                            )
                        }

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

            </div>

        </div>
    )
}