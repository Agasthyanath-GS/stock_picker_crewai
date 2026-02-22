# 📈 StockPicker AI

### Autonomous Multi-Agent Investment Research System Built with CrewAI

**StockPicker AI** is a production-oriented multi-agent system that autonomously discovers trending companies, performs deep financial analysis, selects the strongest investment candidates, and distributes results via email—all while persisting intelligence across sessions using a layered memory architecture.

This project demonstrates applied AI orchestration, structured reasoning, hierarchical delegation, and persistent memory design using the **CrewAI** framework.

---

## 🚀 Why This Project Stands Out

Unlike simple LLM demos, this system showcases:

- 🧠 **Multi-agent coordination** with hierarchical delegation.
- 📊 **Structured financial research** using typed Pydantic models.
- 🧩 **Tool-augmented reasoning** (search + email automation).
- 💾 **Persistent long-term memory** with SQLite.
- 🔎 **Retrieval-Augmented Generation (RAG)** memory.
- 🏗 **Clean separation** of agents, tasks, tools, and configuration.
- 📈 **Production-aware architecture** decisions.

*This is not just a prompt script — it is a fully orchestrated AI system.*

---

## 🏗 System Architecture

### 🔹 Execution Model
The system operates using a **Hierarchical Process** (`Process.hierarchical`). 

In this model:
1. **Manager Agent**: Oversees the entire workflow and delegates tasks.
2. **Worker Agents**: Execute specific investigative or technical tasks.
3. **Aggregation**: Results are refined by the manager before being stored or distributed.

This mirrors real-world organizational structures and enables advanced reasoning workflows.

### 👥 Agent Roles & Capabilities

| Agent | Responsibility | Tools Used |
| :--- | :--- | :--- |
| **Trending Company Finder** | Identifies companies trending in news/market | `SerperDevTool` |
| **Financial Researcher** | Performs deep market & competitive research | `SerperDevTool` |
| **Stock Picker** | Selects best investment & compiles reports | `Custom Email Tool` |
| **Manager** | Delegates, oversees, and validates execution | — |

---

## 📊 Structured AI Outputs

All task outputs are validated using **Pydantic models**, ensuring:
- **Deterministic responses:** No random unstructured text.
- **Type safety:** Reliable hand-offs between agents.
- **Hallucination reduction:** Forced adherence to data schemas.

```python
class TrendingCompany(BaseModel):
    name: str
    ticker: str
    reason: str
```
This transforms unstructured LLM text into reliable, machine-readable data.

---

## 🧠 Memory Architecture (Core Differentiator)

StockPicker AI uses three distinct memory layers to ensure it learns over time:

1. **Short-Term Memory (RAG-Based)**: Maintains contextual continuity during a single execution run using OpenAI embeddings.
2. **Long-Term Memory (SQLite)**: Persists knowledge across different runs (Stored in `./memory/long_term_memory_storage.db`).
3. **Entity Memory**: Tracks company-specific knowledge and builds contextual relationships between different market entities.

> **Why This Matters:** Most AI demos are stateless. This system evolves and retains insights from previous research sessions.

---

## 🛠 Tools & Integration

- **🔎 SerperDevTool**: Used for real-time news discovery and market positioning research.
- **📧 Custom SMTP Email Tool**: Used by the Stock Picker agent to automate the delivery of structured investment reports.

### Environment Variables
To run this system, you need the following keys:
```bash
export OPENAI_API_KEY="your_key"
export SERPER_API_KEY="your_key"
export EMAIL_USER="your_email"
export EMAIL_PASS="your_app_password"
```

---

## 📁 Project Structure

```text
stockpicker/
│
├── output/                          # Output files
│   ├── decision.md                  # Final decision
│   ├── research_report.json         # Final report
│   ├── trending_companies.json      # Summary of the research
├── config/
│   ├── agents.yaml      # Agent personality and goal definitions
│   ├── tasks.yaml       # Task descriptions and expected outputs
│
├── tools/
│   ├── custom_tool.py   # Custom SMTP Email implementation
│
├── memory/
│   ├── long_term_memory_storage.db
│
├── crew.py              # Core logic and crew definition
├── main.py              # Entry point
└── README.md            # You are here
```

---

## 🔄 Execution Flow

1. **Discover** trending companies from live news feeds.
2. **Generate** a structured list of candidates.
3. **Perform** detailed financial and market research.
4. **Evaluate** investment potential based on competitive data.
5. **Select** the strongest candidate.
6. **Email** the final report.
7. **Persist** all findings into long-term memory for future runs.

---

## 🧩 Engineering Decisions

- **Hierarchical Mode**: Chosen to improve coordination logic and enable the system to scale better than rigid sequential pipelines.
- **Structured Outputs**: Ensuring every agent output is a validated object makes the system reliable for production integration.
- **Multi-Layered Memory**: Essential for creating a "research agent" that doesn't start from zero every morning.

---

## 📈 Potential Extensions

- Portfolio performance tracking
- Risk-adjusted scoring algorithms
- Sentiment analysis integration (Twitter/Reddit)
- Automated weekly reporting scheduler
- Dockerized deployment for cloud execution
- Vector database integration (Pinecone / Weaviate)

---

## 🏁 How to Run

1. **Install Dependencies**:
   ```bash
   pip install crewai crewai-tools openai pydantic
   ```
2. **Run the System**:
   ```bash
   crewai run 
   ```

---

## 📚 Skills Demonstrated

- Multi-agent system design
- CrewAI orchestration
- Retrieval-Augmented Generation (RAG)
- Memory architecture design
- Structured AI outputs (Pydantic)
- Tool integration & Automation
- Production-oriented AI engineering

---

## 📜 License
This project is licensed under the **MIT License**.

## 👤 Author
**Agasthyanath G S**  
*AI Engineer & Architecture Enthusiast*

---
*If you're interested in discussing multi-agent AI systems, orchestration frameworks, or applied LLM architecture, feel free to connect!*
