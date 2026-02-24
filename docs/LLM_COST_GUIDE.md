# Understanding LLM Economics 💰

> **LLM Cost Guide** — Part of [AgenticAI Foundry](https://github.com/dlwhyte/AgenticAI_foundry)  
> For MIT Professional Education: Applied Generative AI for Digital Transformation

---

## The Key Insight

> **The same AI transaction can cost between $1 and $230** depending on model choice — a 200x variance!

Before your organization commits to an AI strategy, you need to understand what drives these costs and how to make informed model selection decisions. This guide covers the core concepts behind the LLM Cost Explorer demo.

---

## Tokens: The Currency of AI

### What Is a Token?

A token is the smallest unit of text that an AI model processes. Tokens are **not** the same as words.

| Text | Words | Tokens | Ratio |
|------|-------|--------|-------|
| "Hello" | 1 | 1 | 1:1 |
| "Hello, world!" | 2 | 4 | 1:2 |
| "Artificial intelligence" | 2 | 2 | 1:1 |
| "ChatGPT is amazing" | 3 | 4 | 1:1.3 |
| A typical business email (~200 words) | 200 | ~267 | ~1:1.33 |

**Rules of thumb:**
- 1 token ≈ 4 characters in English
- 1 token ≈ 0.75 words
- 100 tokens ≈ 75 words

### Why Tokens Matter

Every AI API call is billed by token count. Your bill has two parts:

1. **Input tokens** — what you send to the model (your prompt, context, instructions)
2. **Output tokens** — what the model generates back (the response)

**Critical insight:** Output tokens are typically **4x more expensive** than input tokens. This is because generating new text requires sequential computation that can't be parallelized, while reading input can be processed in parallel.

This means a short question with a long answer costs much more than a long question with a short answer.

---

## The Three Cost Drivers

### 1. Model Selection

This is the biggest lever you have. The same prompt sent to different models can vary by **200x** in cost:

| Model | Cost per 1M Input Tokens | Cost per 1M Output Tokens | Relative Cost |
|-------|-------------------------|--------------------------|---------------|
| Gemini 1.5 Flash | $0.075 | $0.30 | 1x (cheapest) |
| GPT-4o-mini | $0.15 | $0.60 | 2x |
| Claude Haiku 4.5 | $1.00 | $5.00 | 13x |
| GPT-4o | $2.50 | $10.00 | 33x |
| Claude Opus 4 | $15.00 | $75.00 | 200x |

**The question isn't "which model is best?" — it's "which model is best for this task?"**

A customer service FAQ bot doesn't need the same intelligence as a medical diagnosis assistant. Matching the model to the task is where cost optimization happens.

### 2. Prompt Length

Longer prompts = more input tokens = higher cost. But prompt engineering is a tradeoff:

- **Short prompts** are cheaper but may produce lower quality or off-target responses
- **Detailed prompts** with examples and instructions cost more but produce better, more consistent results
- **System prompts** are sent with every request — a 500-token system prompt across 100K daily calls adds up fast

### 3. Scale

The economics change dramatically at scale:

| Scale | GPT-4o-mini | GPT-4o | Claude Opus 4 |
|-------|-------------|--------|---------------|
| 1 call | $0.00004 | $0.0006 | $0.004 |
| 1,000 calls/day | $0.04 | $0.60 | $4.00 |
| 100,000 calls/day | $4.00 | $60.00 | $400.00 |
| 1M calls/month | $40.00 | $600.00 | $4,000.00 |

At 1 call, the difference is invisible. At 1M calls/month, it's the difference between a rounding error and a headcount.

---

## The Model Selection Framework

When choosing a model, consider these four dimensions:

### Accuracy vs. Cost

Not every task needs the smartest model. Classify your tasks:

- **Tier 1 — Commodity tasks:** FAQ responses, simple classification, data formatting → Use economy models (GPT-4o-mini, Gemini Flash, Haiku)
- **Tier 2 — Standard tasks:** Content writing, summarization, code generation → Use mid-tier models (GPT-4o, Sonnet, Gemini Pro)
- **Tier 3 — Critical tasks:** Legal analysis, medical reasoning, complex research → Use premium models (Opus, GPT-4 Turbo)

### Latency Requirements

Premium models are often slower. For real-time user-facing applications (chatbots, autocomplete), a faster economy model that responds in 200ms may be better than a premium model that takes 3 seconds.

### Context Window

How much text does the model need to process at once?

- **Short context** (< 4K tokens): Simple Q&A, classification → Any model works
- **Medium context** (4K–32K tokens): Document summarization, email chains → Most models handle this
- **Long context** (32K–1M tokens): Analyzing entire codebases, full legal contracts → Need models with large context windows (Gemini, Claude)

### Data Privacy

- **Cloud APIs** (OpenAI, Anthropic, Google): Data leaves your infrastructure
- **Local models** (Ollama + Llama, Mistral): Data stays on your machine, but lower capability
- **Enterprise agreements**: Many providers offer data retention guarantees for enterprise customers

---

## Using the Cost Explorer Demo

The LLM Cost Explorer in this repo (`pages/1_LLM_Cost_Calculator.py`) lets you:

1. **Count tokens in real-time** — Type or paste text and see exactly how many tokens it produces
2. **Compare models side-by-side** — See cost breakdowns across all major providers
3. **Project costs at scale** — Toggle between 1K, 10K, 100K, and 1M API calls
4. **Export results** — Download CSV or JSON for your assignment write-up

### Running It

```bash
# If running the full app
streamlit run Home.py
# Then click "LLM Cost Calculator" in the sidebar

# Or run it directly
streamlit run pages/1_LLM_Cost_Calculator.py
```

No API key required — the calculator uses tiktoken for local token counting.

---

## Assignment Connection

The Cost Explorer supports your analysis of model pricing at scale. When writing up your findings, consider:

- **What's your use case?** (Customer service, internal ops, content generation?)
- **How many calls per day/month?** (This determines whether model choice matters)
- **What's the accuracy requirement?** (Does a wrong answer cost money or reputation?)
- **What's the latency requirement?** (Real-time chat vs. batch processing?)

A strong analysis names specific models, quantifies the cost difference, and justifies the tradeoff between cost and capability for your organization's use case.

---

## Key Takeaways

1. **Tokens ≠ words** — and output tokens cost 4x more than input tokens
2. **Model selection is the biggest cost lever** — 200x variance between cheapest and most expensive
3. **Match the model to the task** — not every question needs the smartest (and most expensive) model
4. **Scale changes everything** — a trivial per-call difference becomes significant at 100K+ calls/day
5. **Cost is one dimension** — also consider latency, accuracy, context window, and data privacy

---

<p align="center">
  <b>MIT Professional Education | Applied Generative AI for Digital Transformation</b>
</p>
