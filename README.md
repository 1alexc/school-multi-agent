# School Multi‑Agent Demo

A collection of lightweight agents (root, maths, english, computer‑science, geography, …) that can be run with the **ADK** web server.  
Each agent registers tools that perform real HTTP lookups (StackExchange, Rest Countries, Open Trivia DB) and custom Python utilities.

## ▶️ Quick Start

```bash
# 1️⃣ Clone the repo
git clone https://github.com/1alexc/school-multi-agent.git
cd school-multi-agent

# 2️⃣ Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # macOS / Linux
# .\venv\Scripts\activate  # Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt   # ADK, FastAPI, etc.

# 4️⃣ Configure optional API keys (see below)

# 5️⃣ Run the ADK web server (root agent)
./venv/bin/adk run root_agent --host 0.0.0.0 --port 8080
```

Open your browser at `http://localhost:8080` and start chatting. The **root agent** will route queries to the appropriate sub‑agent based on the description strings you see in each `agent.py`.

## 🔧 Required API Keys (optional)

| Service | Why needed? | How to obtain | Environment variable |
|---------|--------------|----------------|----------------------|
| **StackExchange** (StackOverflow) | Fetching recent programming questions (`fetch_programming_question`) | No key required for basic usage, but you can add a `key=` parameter for higher quota. | `STACKEXCHANGE_KEY` |
| **Rest Countries** | Country data (`get_country_info`) | No key required. | – |
| **Open Trivia DB** | Geography trivia (`get_geography_trivia`) | No key required. | – |

If you obtain a StackExchange key, place it in a `.env` file at the project root:

```text
STACKEXCHANGE_KEY=your_key_here
```

The tools automatically read this variable if present.

## 📂 Project Structure (relevant parts)

```
school-multi-agent/
├─ computer_science_agent/
│   ├─ agent.py        # registers explain_algorithm & fetch_programming_question
│   └─ tools.py        # implementations
├─ geography_agent/
│   ├─ agent.py        # registers get_country_info & get_geography_trivia
│   └─ tools.py        # implementations
├─ maths_agent/ …       # existing maths tools
├─ english_agent/ …     # existing english tools
├─ root_agent/
│   └─ agent.py        # coordinator, routes based on descriptions
├─ requirements.txt
└─ README.md           # <-- you are reading it!
```

## 🛠️ Adding New Tools / Agents

1. **Create `tools.py`** in the new agent folder.  
2. **Expose functions** (return a dict with `status` and payload).  
3. **Import them** in `agent.py` and add them to the `tools=` list.  
4. **Update the agent description** so the root agent can route queries correctly.

## 📈 Rate‑Limit Note

The free tier of Gemini‑2.5‑Flash and the external APIs have daily quotas.  
If you hit a limit, wait until the quota resets or switch to a paid plan.

---

Enjoy experimenting with the agents! If you have questions, open an issue or submit a pull request.