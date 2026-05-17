import { useEffect, useRef, useState } from "react";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

import { Prism as SyntaxHighlighter }
from "react-syntax-highlighter";

import { vscDarkPlus }
from "react-syntax-highlighter/dist/esm/styles/prism";

export default function ChatPanel() {

    const [messages, setMessages] = useState([]);

    const [input, setInput] = useState("");

    const [loading, setLoading] = useState(false);

    const bottomRef = useRef(null);

    useEffect(() => {

        bottomRef.current?.scrollIntoView({
            behavior: "smooth"
        });

    }, [messages]);

    async function sendMessage() {

        if (!input.trim() || loading) {
            return;
        }

        const userMessage = {
            role: "user",
            content: input
        };

        setMessages(prev => [
            ...prev,
            userMessage
        ]);

        const currentPrompt = input;

        setInput("");

        setLoading(true);

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/chat",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        prompt: currentPrompt
                    })
                }
            );

            const data = await response.json();

            setMessages(prev => [

                ...prev,

                {
                    role: "assistant",
                    content:
                        typeof data.response === "string"
                            ? data.response
                            : JSON.stringify(
                                data,
                                null,
                                2
                            )
                }
            ]);

        }

        catch (error) {

            setMessages(prev => [

                ...prev,

                {
                    role: "assistant",
                    content:
`# Backend Error

\`\`\`
${error.message}
\`\`\`
`
                }
            ]);
        }

        setLoading(false);
    }

    return (

        <div
            style={{
                flex: 1,
                display: "flex",
                flexDirection: "column",
                background: "#000"
            }}
        >

            <div
                style={{
                    flex: 1,
                    overflowY: "auto",
                    padding: "40px",
                    display: "flex",
                    flexDirection: "column",
                    gap: "40px"
                }}
            >

                {

                    messages.length === 0 && (

                        <div
                            style={{
                                color: "#777",
                                fontSize: "18px"
                            }}
                        >
                            HELIX ready.
                        </div>
                    )
                }

                {messages.map((message, index) => (

                    <div
                        key={index}
                        style={{
                            display: "flex",
                            justifyContent:
                                message.role === "user"
                                    ? "flex-end"
                                    : "flex-start"
                        }}
                    >

                        {

                            message.role === "user"

                            ?

                            <div
                                style={{
                                    maxWidth: "520px",
                                    background: "#1b1b1b",
                                    border: "1px solid #2a2a2a",
                                    borderRadius: "22px",
                                    padding: "18px 22px",
                                    color: "white",
                                    lineHeight: "1.7"
                                }}
                            >
                                {message.content}
                            </div>

                            :

                            <div
                                style={{
                                    width: "100%",
                                    maxWidth: "900px",
                                    color: "white",
                                    lineHeight: "1.8",
                                    fontSize: "16px"
                                }}
                            >

                                <ReactMarkdown

                                    remarkPlugins={[remarkGfm]}

                                    components={{

                                        code({

                                            inline,
                                            className,
                                            children,
                                            ...props

                                        }) {

                                            const match =
                                                /language-(\w+)/.exec(
                                                    className || ""
                                                );

                                            return !inline && match ? (

                                                <SyntaxHighlighter

                                                    style={vscDarkPlus}

                                                    language={match[1]}

                                                    PreTag="div"

                                                    customStyle={{
                                                        borderRadius: "18px",
                                                        padding: "18px",
                                                        background: "#0d1117",
                                                        border:
                                                        "1px solid #222"
                                                    }}

                                                    {...props}
                                                >
                                                    {
                                                        String(children)
                                                        .replace(/\n$/, "")
                                                    }
                                                </SyntaxHighlighter>

                                            ) : (

                                                <code
                                                    style={{
                                                        background: "#111",
                                                        padding: "4px 8px",
                                                        borderRadius: "8px"
                                                    }}
                                                    {...props}
                                                >
                                                    {children}
                                                </code>
                                            );
                                        }
                                    }}

                                >
                                    {message.content}
                                </ReactMarkdown>

                            </div>
                        }

                    </div>

                ))}

                {

                    loading && (

                        <div
                            style={{
                                color: "#00ff88"
                            }}
                        >
                            HELIX thinking...
                        </div>
                    )
                }

                <div ref={bottomRef} />

            </div>

            <div
                style={{
                    borderTop: "1px solid #1f1f1f",
                    padding: "24px",
                    display: "flex",
                    gap: "18px",
                    background: "#050505"
                }}
            >

                <input
                    value={input}

                    onChange={(e) =>
                        setInput(e.target.value)
                    }

                    onKeyDown={(e) => {

                        if (e.key === "Enter") {
                            sendMessage();
                        }
                    }}

                    placeholder="Message HELIX..."

                    style={{
                        flex: 1,
                        height: "62px",
                        borderRadius: "18px",
                        border: "1px solid #1f1f1f",
                        background: "#0d0d0d",
                        color: "white",
                        padding: "0 22px",
                        outline: "none",
                        fontSize: "16px"
                    }}
                />

                <button
                    onClick={sendMessage}

                    style={{
                        width: "120px",
                        borderRadius: "18px",
                        border: "none",
                        background: "white",
                        color: "black",
                        fontWeight: "700",
                        fontSize: "16px",
                        cursor: "pointer"
                    }}
                >
                    Send
                </button>

            </div>

        </div>
    );
}