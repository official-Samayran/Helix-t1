# 🚀 H E L I X

> Autonomous Local AI Operating System

---

# 📖 Overview

H E L I X is a modular AI system designed for intelligent automation, local AI execution, autonomous task handling, and advanced developer workflows.

It combines:
- 🧠 Local LLMs
- ⚡ Autonomous execution
- 🤖 Multi-agent systems
- 🛠 Tool orchestration
- 💾 Memory systems
- 🌐 API-based architecture
- 🔒 Secure execution environments

H E L I X is built to:
- Think
- Plan
- Execute
- Automate
- Assist in real workflows

All locally.

---

# ✨ Features

- 🧠 Local AI models using Ollama
- ⚡ Autonomous orchestration engine
- 🤖 Multi-agent architecture
- 🌐 API server support
- 🔒 Secure sandboxed execution
- 🐍 Python automation support
- 🛠 Extensible tools system
- 🧩 Modular architecture
- 📡 Offline-capable workflows
- 🚀 Fast local inference

---

# 🏗 System Architecture

```text
                    ┌────────────────────┐
                    │       USER         │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │     API SERVER     │
                    │   Flask/FastAPI    │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │    ORCHESTRATOR    │
                    │    Main Brain      │
                    └─────────┬──────────┘
              ┌───────────────┼────────────────┐
              ▼               ▼                ▼
     ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
     │ MEMORY CORE  │ │ TOOL SYSTEM  │ │ AGENT LAYER  │
     └──────────────┘ └──────────────┘ └──────────────┘
              │               │                │
              ▼               ▼                ▼
     ┌──────────────────────────────────────────────┐
     │              LOCAL LLMs (OLLAMA)            │
     │   DeepSeek / Phi / Mistral / Llama Models   │
     └──────────────────────────────────────────────┘
```

---

# 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python |
| API | Flask / FastAPI |
| AI Runtime | Ollama |
| Models | DeepSeek, Phi, Llama |
| Execution | Python subprocess |
| Memory | JSON / Vector-ready |
| Automation | Custom tools |
| OS Support | Windows |

---

# 📂 Folder Structure

```text
HELIX/
│
├── api/                # API routes and server
├── core/               # Main orchestration logic
├── agents/             # AI agents
├── tools/              # Tool execution modules
├── memory/             # Memory systems
├── models/             # Model configs
├── prompts/            # System prompts
├── config/             # Config files
├── tests/              # Testing
├── main.py             # Entry point
├── requirements.txt
└── README.md
```

---

# 💻 Hardware Requirements

## Minimum
- Intel i5 8th Gen
- 8GB RAM
- 10GB free storage

## Recommended
- Intel i5 12th Gen or higher
- 16GB+ RAM
- NVIDIA GPU
- SSD storage

---

# ⚙ Full Setup Guide (Fresh PC)

## 1️⃣ Install Python

Download Python:

https://www.python.org/downloads/

During installation:
- ✅ ENABLE `Add Python to PATH`

Verify installation:

```bash
python --version
```

---

## 2️⃣ Install Git

Download Git:

https://git-scm.com/downloads

Verify installation:

```bash
git --version
```

---

## 3️⃣ Install Ollama

Download Ollama:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

---

# 4️⃣ Install AI Models

Install models:

```bash
ollama pull phi3.5
```

```bash
ollama pull deepseek-coder-v2:lite
```

Optional:

```bash
ollama list
```

---

# 5️⃣ Clone H E L I X

```bash
git clone https://github.com/samayran-ik/Helix.git
```

```bash
cd Helix
```

---

# 6️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

## Windows

```bash
venv\Scripts\activate
```

---

# 7️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 8️⃣ Configure Environment

Create a `.env` file:

```env
OLLAMA_BASE_URL=http://localhost:11434
MODEL_NAME=phi3.5
SAFE_WORKSPACE=E:\Helix_Projects
```

---

# 9️⃣ Start Ollama

```bash
ollama serve
```

Keep terminal open.

---

# 🔟 Run H E L I X

Open another terminal:

```bash
python main.py
```

If using FastAPI:

```bash
uvicorn api.server:app --reload
```

---

# 🧪 First Test

```bash
curl -X POST http://127.0.0.1:5000/execute ^
-H "Content-Type: application/json" ^
-d "{\"command\":\"Create a python calculator app\"}"
```

---

# 🧠 Recommended Models

| Model | Use |
|---|---|
| phi3.5 | Lightweight assistant |
| deepseek-coder-v2 | Coding |
| mistral | General reasoning |
| llama3 | Large conversations |

---

# 🔒 Security Notes

H E L I X can execute code.

Never:
- ❌ expose server publicly
- ❌ run unknown commands
- ❌ disable path restrictions
- ❌ allow unrestricted shell access

Recommended:
- ✅ isolated workspace
- ✅ non-admin Windows account
- ✅ firewall restrictions

---

# 🩹 Troubleshooting

## Ollama Not Found

```bash
ollama --version
```

Reinstall Ollama if missing.

---

## Python Not Found

Reinstall Python and enable:
- ✅ `Add Python to PATH`

---

## Port Already In Use

Check process:

```bash
netstat -ano | findstr :5000
```

Kill process:

```bash
taskkill /PID <PID> /F
```

---

## Dependency Errors

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

---

# 🛣 Future Roadmap

- 🎙 Voice interaction
- 🖥 GUI dashboard
- 🤖 Multi-agent collaboration
- 🧠 Long-term memory
- 🌐 Browser automation
- 👁 Vision capabilities
- 📱 Mobile integration
- ⚡ Autonomous workflows

---

# 🧬 Philosophy

H E L I X is designed to be:
- 🧩 modular
- 🔒 local-first
- ⚡ execution-capable
- 🛡 privacy-focused
- 🔧 extensible
- 🤖 automation-ready

Not just conversational.

Built for real execution.

---

# 👨‍💻 Author

Built by Samayran

GitHub:
https://github.com/samayran-ik

---

# 📜 License

MIT License

Use freely.  
Modify freely.  
Build freely.
