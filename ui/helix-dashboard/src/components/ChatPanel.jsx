import { useState } from "react"

import axios from "axios"

import ReactMarkdown from "react-markdown"

import remarkGfm from "remark-gfm"

import { Prism as SyntaxHighlighter }
from "react-syntax-highlighter"

import { vscDarkPlus }
from "react-syntax-highlighter/dist/esm/styles/prism"


export default function ChatPanel() {

    const [messages, setMessages] = useState([])

    const [input, setInput] = useState("")

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

            const response = await axios.post(
                "http://127.0.0.1:8000/chat",
                {
                    prompt: userInput
                }
            )

            let content =
                response.data.response

            if (
                typeof content === "object"
            ) {

                content = `\`\`\`json
${JSON.stringify(
    content,
    null,
    2
)}
\`\`\``
            }

            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    content
                }
            ])

        } catch (error) {

            console.error(error)

            setMessages(prev => [
                ...prev,
                {
                    role: "assistant",
                    content:
                        "## Backend Error\n\nConnection failed."
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
                            components={{

                                code({
                                    inline,
                                    className,
                                    children,
                                    ...props
                                }) {

                                    const match =
                                        /language-(\\w+)/.exec(
                                            className || ''
                                        )

                                    return !inline && match ? (

                                        <SyntaxHighlighter
                                            style={vscDarkPlus}
                                            language={match[1]}
                                            PreTag="div"
                                            {...props}
                                        >
                                            {String(children).replace(/\\n$/, '')}
                                        </SyntaxHighlighter>

                                    ) : (

                                        <code
                                            className={className}
                                            {...props}
                                        >
                                            {children}
                                        </code>
                                    )
                                }
                            }}
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
                        setInput(e.target.value)
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