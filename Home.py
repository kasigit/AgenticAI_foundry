"""
AgenticAI Foundry - Home Page
MIT Professional Education: Applied Generative AI for Digital Transformation
"""

import streamlit as st

st.set_page_config(
    page_title="AgenticAI Foundry",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A5F;
        margin-bottom: 0.3rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #555;
        margin-bottom: 1.5rem;
    }
    .welcome-box {
        background: linear-gradient(135deg, #1E3A5F 0%, #2d6a9f 100%);
        color: white;
        padding: 1.5rem 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
    }
    .module-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.25rem 1.5rem;
        margin-bottom: 1rem;
        border-left: 5px solid #1E3A5F;
        height: 100%;
    }
    .module-card h4 {
        color: #1E3A5F;
        margin-bottom: 0.4rem;
    }
    .module-card p {
        color: #444;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
    }
    .badge {
        display: inline-block;
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 600;
        margin-right: 0.3rem;
    }
    .badge-green  { background: #d4edda; color: #155724; }
    .badge-blue   { background: #cce5ff; color: #004085; }
    .badge-orange { background: #fff3cd; color: #856404; }
    .path-card {
        border-radius: 10px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 0.75rem;
    }
    .path-docker { background: #e8f4fd; border-left: 5px solid #2196F3; }
    .path-python { background: #f3e8fd; border-left: 5px solid #9C27B0; }
    .tip-box {
        background: #fff8e1;
        border-left: 4px solid #FFC107;
        padding: 1rem 1.25rem;
        border-radius: 8px;
        margin-top: 1rem;
    }
    .footer {
        text-align: center;
        color: #888;
        font-size: 0.85rem;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #eee;
    }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<p class="main-header">🤖 AgenticAI Foundry</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-header">MIT Professional Education · Applied Generative AI for Digital Transformation</p>',
    unsafe_allow_html=True
)

# ── Welcome Box ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="welcome-box">
    <h3 style="margin-bottom:0.4rem;">👋 Welcome to the Course Demo Platform</h3>
    <p style="font-size:1.05rem; margin-bottom:0.3rem;">
        This platform gives you hands-on experience with the AI concepts covered in each module.
        No deep technical background required — just pick a demo from the sidebar and explore.
    </p>
    <p style="margin:0; font-size:0.95rem; opacity:0.9;">
        📥 First time here? Download the
        <a href="https://github.com/dlwhyte/AgenticAI_foundry/blob/main/docs/Student_Quick_Start.pdf"
           style="color:#FFD700; font-weight:600;" target="_blank">Student Quick Start Guide</a>
        before you begin.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Module Cards ──────────────────────────────────────────────────────────────
st.markdown("### 📚 Course Demos — What's Available")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="module-card">
        <h4>💰 Module 1 · LLM Cost Explorer</h4>
        <p>Discover why the same AI task can cost anywhere from $1 to $230 depending on the model you choose.
        Compare 10+ models across OpenAI, Anthropic, and Google in real time.</p>
        <span class="badge badge-green">✅ No API key needed</span>
        <span class="badge badge-green">✅ No setup required</span>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/1_LLM_Cost_Calculator.py", label="→ Open LLM Cost Explorer", icon="💰")

with col2:
    st.markdown("""
    <div class="module-card">
        <h4>🤖 Module 2 · Multi-Agent Demo (CrewAI)</h4>
        <p>Watch three AI agents — Researcher, Writer, and Editor — collaborate on a task in real time.
        See how multi-agent systems divide work just like a team of employees.</p>
        <span class="badge badge-orange">⚠️ Requires Ollama or OpenAI key</span>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/2_Multi_Agent_Demo.py", label="→ Open Multi-Agent Demo", icon="🤖")

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="module-card">
        <h4>🔗 Module 2 · LangChain Agent Demo</h4>
        <p>See a single AI agent use web search to answer questions in real time.
        Compare this approach to the multi-agent CrewAI pattern — two different ways to build AI systems.</p>
        <span class="badge badge-orange">⚠️ Requires Ollama or OpenAI key</span>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/3_LangChain_Agent_Demo.py", label="→ Open LangChain Demo", icon="🔗")

with col4:
    st.markdown("""
    <div class="module-card">
        <h4>🔌 Module 3 · MCP Explorer</h4>
        <p>Understand how AI agents connect to external tools like calendars, CRMs, and databases
        using the Model Context Protocol — the new standard for AI integrations.</p>
        <span class="badge badge-green">✅ No API key needed</span>
        <span class="badge badge-green">✅ No setup required</span>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/4_MCP_Explorer.py", label="→ Open MCP Explorer", icon="🔌")

col5, col6 = st.columns(2)

with col5:
    st.markdown("""
    <div class="module-card">
        <h4>🛡️ Module 4 · Agent Security Demo</h4>
        <p>Explore prompt injection attacks and defense mechanisms hands-on. Launch real attacks
        against a customer service agent, then watch guardrails intercept them in real time.
        Understand why AI security is a business-critical concern.</p>
        <span class="badge badge-green">✅ Demo Mode requires no API key</span>
        <span class="badge badge-orange">⚠️ Live Mode requires Ollama, OpenAI, or Anthropic</span>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/5_Agent_Security_Demo.py", label="→ Open Security Demo", icon="🛡️")

with col6:
    st.markdown("""
    <div class="module-card" style="border-left-color: #ccc; background: #f8f8f8;">
        <h4 style="color: #999;">🔜 More Modules Coming</h4>
        <p style="color: #999;">Additional demos will appear here as the course progresses.
        Check back after each module session.</p>
    </div>
    """, unsafe_allow_html=True)

# ── Setup Paths ───────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("### 🚀 How to Run This App — Choose Your Path")

st.markdown("""
<div class="path-card path-docker">
    <strong>🐳 Path A · Docker (Recommended for most students)</strong><br/>
    <span style="font-size:0.9rem; color:#555;">
        Docker packages the entire app into a self-contained box — no worrying about Python versions or conflicting software.
        Once installed, it runs the same on every computer.<br/><br/>
        <strong>Best if:</strong> You want the most reliable setup with the fewest moving parts.<br/>
        <strong>Time:</strong> ~20 minutes on first run (mostly waiting for downloads).<br/>
        <strong>Guide:</strong> See <code>docs/DOCKER_GUIDE.md</code> in the repo, or the Student Quick Start PDF.
    </span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="path-card path-python">
    <strong>🐍 Path B · Python (Alternative)</strong><br/>
    <span style="font-size:0.9rem; color:#555;">
        Run the app directly using Python on your computer. More steps to set up but gives you
        more visibility into how everything works.<br/><br/>
        <strong>⚠️ Version requirement:</strong> You need Python 3.10 or higher.
        Run <code>python3 --version</code> in your terminal first —
        if it shows 3.9 or lower, use Docker instead.<br/><br/>
        <strong>Best if:</strong> You have Python 3.10+ installed or want to explore the code.<br/>
        <strong>Time:</strong> ~15 minutes, but more steps that can go wrong.<br/>
        <strong>Guide:</strong> See <code>docs/BEGINNERS_GUIDE.md</code> in the repo.
    </span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="tip-box">
    💡 <strong>Not sure which to pick?</strong> If you've never used Docker or Python before,
    we recommend <strong>Docker</strong> — it has a bigger one-time install but is much more
    reliable once running. Download the <strong>Student Quick Start PDF</strong> from the repo's
    <code>docs/</code> folder for step-by-step screenshots.
</div>
""", unsafe_allow_html=True)

# ── Quick Environment Check ───────────────────────────────────────────────────
st.markdown("---")
st.markdown("### 🔍 Quick Environment Status")

import os

col_a, col_b, col_c = st.columns(3)

with col_a:
    openai_key = bool(os.environ.get("OPENAI_API_KEY"))
    if openai_key:
        st.success("✅ OpenAI API Key detected")
    else:
        st.info("ℹ️ No OpenAI key set — Ollama mode available")

with col_b:
    try:
        import urllib.request
        urllib.request.urlopen("http://localhost:11434/api/tags", timeout=2)
        st.success("✅ Ollama is running")
    except Exception:
        try:
            urllib.request.urlopen("http://host.docker.internal:11434/api/tags", timeout=2)
            st.success("✅ Ollama is running (Docker)")
        except Exception:
            st.info("ℹ️ Ollama not detected — needed for agent demos")

with col_c:
    try:
        import crewai
        st.success("✅ CrewAI installed")
    except ImportError:
        st.info("ℹ️ CrewAI not installed — needed for Module 2")

st.caption("These checks only affect the agent demos (Module 2). Modules 1 and 3 work without any of the above.")

# ── Help & Resources ──────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("### 📖 Help & Documentation")

r1, r2, r3 = st.columns(3)
with r1:
    st.markdown("""
    **🆕 New to everything?**
    Start with the Student Quick Start PDF in `docs/` — it walks you through downloading
    and running the app with screenshots, no experience needed.
    """)
with r2:
    st.markdown("""
    **🐳 Docker questions?**
    See `docs/DOCKER_GUIDE.md` for a plain-English walkthrough of every Docker step,
    including common error messages and how to fix them.
    """)
with r3:
    st.markdown("""
    **🤖 Agent demo setup?**
    See `docs/CREWAI_SETUP.md` for Ollama and OpenAI setup, model recommendations,
    and troubleshooting for the Module 2 demos.
    """)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    MIT Professional Education · Applied Generative AI for Digital Transformation<br/>
    Modules 1 &amp; 3 require no API key · Module 2 demos require Ollama or an OpenAI key
</div>
""", unsafe_allow_html=True)
