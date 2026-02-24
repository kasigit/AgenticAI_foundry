# Understanding Multi-Agent Systems 🤖

> **Multi-Agent Guide** — Part of [AgenticAI Foundry](https://github.com/dlwhyte/AgenticAI_foundry)  
> For MIT Professional Education: Applied Generative AI for Digital Transformation

---

## Two Approaches to AI Agents

This repo includes two Module 2 demos that show fundamentally different ways to build AI agents. Understanding the difference helps you decide which pattern fits your business problem.

| | CrewAI (Multi-Agent) | LangChain (Single Agent) |
|---|---------------------|--------------------------|
| **Metaphor** | A team of specialists | One person with a toolbox |
| **Demo** | Multi-Agent Demo | LangChain Agent Demo |
| **Pattern** | Researcher → Writer → Editor | Think → Search → Answer |
| **Best for** | Complex workflows with distinct stages | Real-time data retrieval and reasoning |

---

## The Single-Agent Pattern (LangChain)

### How It Works

A single AI agent receives a question, reasons about what it needs to do, uses tools to get information, and delivers an answer. This is called the **ReAct pattern** — Reasoning + Acting.

```
User Question
    ↓
🤔 Thought:  "I need to look up the current Bitcoin price"
    ↓
🔧 Action:   [calls web search tool]
    ↓
👁️ Observe:  "Bitcoin is trading at $97,432"
    ↓
🤔 Thought:  "Now I need Ethereum's price too"
    ↓
🔧 Action:   [calls web search tool again]
    ↓
👁️ Observe:  "Ethereum is trading at $3,241"
    ↓
💬 Answer:   "Bitcoin is at $97,432 and Ethereum is at $3,241..."
```

The agent decides **on its own** when to use tools, what to search for, and when it has enough information to answer.

### When to Use Single Agents

- **Real-time data lookups** — current prices, weather, news
- **Simple question-answering** — one question, one answer
- **Tool-augmented chat** — a chatbot that can search, calculate, or query databases
- **Quick tasks** — where a single perspective is sufficient

### The Demo: Crypto Price Agent

The LangChain Agent Demo (`pages/3_LangChain_Agent_Demo.py`) uses:

- **LangChain** as the agent framework
- **DuckDuckGo Search** as the tool
- **ReAct pattern** for reasoning
- **Ollama or OpenAI** as the AI "brain"

```bash
# Run it
streamlit run Home.py
# Then click "LangChain Agent Demo" in the sidebar
```

---

## The Multi-Agent Pattern (CrewAI)

### How It Works

Instead of one agent doing everything, you create a **team of specialists** — each with a defined role, goal, and backstory. They pass work to each other in sequence, like an assembly line.

```
User Request: "Research AI in healthcare"
    ↓
🔬 Researcher Agent
    Role: "Research Analyst"
    → Gathers facts, stats, case studies
    → Output: Detailed research notes
    ↓
✍️ Writer Agent
    Role: "Content Writer"
    → Transforms research into a clear brief
    → Output: 300-500 word draft
    ↓
📝 Editor Agent
    Role: "Editor"
    → Polishes for clarity, accuracy, professionalism
    → Output: Final, publication-ready brief
```

Each agent only sees the output of the previous agent — they're specialists, not generalists.

### Agent Specialization

CrewAI agents are defined with three attributes that shape their behavior:

```python
Agent(
    role="Research Analyst",           # Their job title
    goal="Gather comprehensive info",  # What they're trying to achieve
    backstory="You are an experienced  # Shapes their personality and approach
              researcher with 10 years
              of experience in data
              analysis..."
)
```

CrewAI combines these attributes with the task description to construct the actual prompt sent to the LLM. You define **who the agent is**, and CrewAI handles **how to instruct them**.

This is powerful because:
- The **Researcher** is told to dig deep and find facts — it doesn't try to write polished prose
- The **Writer** receives research notes and focuses on clarity — it doesn't second-guess the research
- The **Editor** focuses purely on polish — it doesn't add new information

### When to Use Multi-Agent Systems

- **Complex workflows with distinct stages** — research → analysis → writing → review
- **Tasks requiring different skills** — one agent can't be expert at everything
- **Quality control** — each agent checks the previous agent's work
- **Separation of concerns** — you can tune each agent independently

### The Demo: Research Crew

The Multi-Agent Demo (`pages/2_Multi_Agent_Demo.py`) uses:

- **CrewAI** as the orchestration framework
- **Three specialized agents** — Researcher, Writer, Editor
- **Sequential task handoff** — each agent builds on the previous agent's work
- **Ollama or OpenAI** as the AI "brain"

```bash
# Run via Streamlit
streamlit run Home.py
# Then click "Multi-Agent Demo" in the sidebar

# Or run via command line
python -m crews.research_crew --provider ollama --task "Research AI in healthcare"
```

---

## Comparing the Two Approaches

### Performance Characteristics

| Metric | Single Agent (LangChain) | Multi-Agent (CrewAI) |
|--------|-------------------------|---------------------|
| **Speed** | Faster (one agent, fewer calls) | Slower (3+ agents, sequential) |
| **Cost** | Lower (fewer tokens) | Higher (each agent uses tokens) |
| **Quality** | Good for focused tasks | Better for complex, multi-step tasks |
| **Reliability** | Can get stuck in loops | More predictable with defined handoffs |
| **Complexity** | Simple to set up | More setup, but more control |

### Real-World Analogies

**Single Agent = A freelancer.** You give them a task, they figure out how to do it, they deliver. Fast and cheap, but limited by one person's perspective.

**Multi-Agent = A team.** The researcher doesn't write copy, the writer doesn't do editing. Each person does what they're best at. Slower and more expensive, but higher quality for complex work.

### Decision Framework

Choose **single agent** when:
- The task is straightforward (look something up, answer a question)
- Speed matters more than depth
- Budget is tight
- You need real-time responses

Choose **multi-agent** when:
- The task has multiple distinct phases
- Quality and thoroughness matter more than speed
- Different expertise is needed at each stage
- You want built-in quality control (each agent reviews previous work)

---

## Telemetry: What to Watch

Both demos show telemetry data — pay attention to these metrics:

| Metric | What It Tells You |
|--------|------------------|
| **Duration** | How long the task took end-to-end |
| **Total Tokens** | The raw cost driver — input + output tokens across all agents |
| **Tool Calls** | How many times the agent used external tools |
| **Estimated Cost** | Approximate USD cost of the API calls |

For the multi-agent demo, notice how the total token count is **much higher** than the single-agent demo for a comparable task. Each agent in the crew consumes tokens independently. This is the cost of specialization — better results, but more expensive.

---

## Provider Options

Both demos support two AI providers:

### Ollama (Free, Local)

Run AI models on your own machine. No data leaves your computer. Free to use, but speed depends on your hardware.

```bash
# Install
brew install ollama          # macOS
curl -fsSL https://ollama.ai/install.sh | sh  # Linux

# Download a model
ollama pull llama3.2

# Start the server (keep running)
ollama serve
```

### OpenAI (Paid, Cloud)

Faster and more capable, but costs money and sends data to OpenAI's servers.

```bash
# Set your API key
export OPENAI_API_KEY="sk-your-key-here"
```

For detailed setup instructions, see the [CrewAI Setup Guide](CREWAI_SETUP.md) or the [Beginner's Guide](BEGINNERS_GUIDE.md).

---

## Assignment Connection

The agent demos support your analysis of single-agent vs multi-agent patterns. When writing about agents, consider:

- **Which pattern fits your use case?** A customer service bot is probably single-agent. A content production pipeline is probably multi-agent.
- **What's the cost/quality tradeoff?** Multi-agent produces better results but costs 3-5x more in tokens.
- **What telemetry would you monitor?** Duration, token usage, error rates, user satisfaction.
- **How would agents specialize?** What roles, goals, and backstories would you define?

---

## Key Takeaways

1. **Single agents** are fast and cheap — ideal for focused, real-time tasks with tool access
2. **Multi-agent crews** produce higher quality output — ideal for complex, multi-stage workflows
3. **Specialization is the key insight** — agents with narrow roles outperform general-purpose agents
4. **Telemetry matters** — token usage, duration, and cost should inform your model and architecture choices
5. **Start simple** — begin with a single agent, add agents only when the task genuinely benefits from specialization

---

<p align="center">
  <b>MIT Professional Education | Applied Generative AI for Digital Transformation</b>
</p>
