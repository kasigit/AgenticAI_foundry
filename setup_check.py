"""
AgenticAI Foundry — Environment Setup Checker
MIT Professional Education: Applied Generative AI for Digital Transformation

Run this script to check whether your environment is ready to run the demos.
Usage:  python setup_check.py

It checks:
  - Python version
  - Required Python libraries
  - Docker availability
  - Ollama availability
  - OpenAI API key
"""

import sys
import os
import importlib
import subprocess

# ── Colours for terminal output ───────────────────────────────────────────────
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
BLUE   = "\033[94m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def ok(msg):    print(f"  {GREEN}✅ {msg}{RESET}")
def warn(msg):  print(f"  {YELLOW}⚠️  {msg}{RESET}")
def fail(msg):  print(f"  {RED}❌ {msg}{RESET}")
def info(msg):  print(f"  {BLUE}ℹ️  {msg}{RESET}")
def header(msg): print(f"\n{BOLD}{msg}{RESET}")
def divider():   print("─" * 55)


def check_python():
    header("1. Python Version")
    major, minor = sys.version_info.major, sys.version_info.minor
    version_str = f"Python {major}.{minor}.{sys.version_info.micro}"
    if major == 3 and minor >= 10:
        ok(f"{version_str} — good to go")
    elif major == 3 and minor == 9:
        warn(f"{version_str} — Python 3.9 is too old for the agent demos (Module 2)")
        warn("CrewAI requires Python 3.10 or higher")
        info("Options: upgrade Python OR use Docker instead")
        info("Modules 1 and 3 will still work fine with Python 3.9")
        info("Upgrade Python: https://www.python.org/downloads/")
    else:
        fail(f"{version_str} — Python 3.10 or higher is required")
        fail("Use Docker instead, or upgrade: https://www.python.org/downloads/")


def check_libraries():
    header("2. Required Python Libraries")

    # Core libraries (Modules 1 & 3 — no API key needed)
    core = {
        "streamlit":  "Streamlit (the web app framework)",
        "plotly":     "Plotly (interactive charts)",
        "pandas":     "Pandas (data handling)",
        "numpy":      "NumPy (number crunching)",
        "tiktoken":   "Tiktoken (token counting for Module 1)",
    }

    # Agent libraries (Module 2 — optional)
    agent = {
        "crewai":              "CrewAI (multi-agent orchestration)",
        "langchain_community": "LangChain Community (agent tools)",
        "langchain_openai":    "LangChain OpenAI (OpenAI connector)",
    }

    print("\n  Core libraries (needed for Modules 1 & 3):")
    all_core_ok = True
    for lib, label in core.items():
        try:
            importlib.import_module(lib)
            ok(label)
        except ImportError:
            fail(f"{label} — not installed")
            all_core_ok = False

    if not all_core_ok:
        info("Fix: run  pip install -r requirements.txt")

    print("\n  Agent libraries (needed for Module 2 demos):")
    all_agent_ok = True
    for lib, label in agent.items():
        try:
            importlib.import_module(lib)
            ok(label)
        except ImportError:
            warn(f"{label} — not installed (only needed for Module 2)")
            all_agent_ok = False

    if not all_agent_ok:
        info("Fix: run  pip install -r requirements-crewai.txt")


def check_docker():
    header("3. Docker")
    try:
        result = subprocess.run(
            ["docker", "--version"],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            version = result.stdout.strip()
            ok(f"Docker installed — {version}")

            # Check if Docker daemon is running
            daemon = subprocess.run(
                ["docker", "info"],
                capture_output=True, text=True, timeout=10
            )
            if daemon.returncode == 0:
                ok("Docker Desktop is running and ready")
            else:
                warn("Docker is installed but Docker Desktop is not running")
                info("Fix: Open the Docker Desktop application and wait for the whale icon to stop animating")
        else:
            fail("Docker command failed — may not be installed correctly")
    except FileNotFoundError:
        warn("Docker not found — this is fine if you are using the Python path")
        info("If you want to use Docker: download from https://www.docker.com/products/docker-desktop/")
    except subprocess.TimeoutExpired:
        warn("Docker check timed out — Docker Desktop may still be starting up")


def check_ollama():
    header("4. Ollama (free local AI — needed for Module 2 without OpenAI key)")
    import urllib.request
    import urllib.error

    hosts_to_try = [
        ("http://localhost:11434",          "localhost"),
        ("http://host.docker.internal:11434", "Docker internal host"),
    ]

    custom_host = os.environ.get("OLLAMA_HOST")
    if custom_host:
        hosts_to_try.insert(0, (custom_host, f"OLLAMA_HOST env var ({custom_host})"))

    found = False
    for host, label in hosts_to_try:
        try:
            req = urllib.request.Request(f"{host}/api/tags", method="GET")
            with urllib.request.urlopen(req, timeout=3) as resp:
                if resp.status == 200:
                    import json
                    data = json.loads(resp.read().decode())
                    models = [m["name"] for m in data.get("models", [])]
                    ok(f"Ollama is running ({label})")
                    if models:
                        ok(f"Models available: {', '.join(models)}")
                    else:
                        warn("Ollama is running but no models downloaded yet")
                        info("Fix: run  ollama pull llama3.2  (downloads ~2GB)")
                    found = True
                    break
        except Exception:
            continue

    if not found:
        warn("Ollama is not running or not installed")
        info("This only matters for Module 2 demos without an OpenAI key")
        info("To install: download from https://ollama.ai")
        info("To start:   run  ollama serve  in a terminal")


def check_openai():
    header("5. OpenAI API Key")
    key = os.environ.get("OPENAI_API_KEY", "")
    if key and key.startswith("sk-") and len(key) > 20:
        ok(f"OpenAI API key detected (ending in ...{key[-4:]})")
        info("This enables the paid OpenAI option in Module 2 demos")
    elif key:
        warn("OPENAI_API_KEY is set but looks unusual — double-check the value")
    else:
        info("No OpenAI API key set — this is fine")
        info("Modules 1 & 3 don't need it. Module 2 can use Ollama instead.")
        info("To set it later: enter your key directly in the app sidebar")


def summary(results: dict):
    header("Summary")
    divider()

    if results.get("modules_1_3"):
        ok("Modules 1 & 3 (Cost Explorer + MCP Explorer) — ready to run")
    else:
        fail("Modules 1 & 3 — missing core libraries (run: pip install -r requirements.txt)")

    if results.get("module_2_ollama") or results.get("module_2_openai"):
        ok("Module 2 demos — ready to run")
    else:
        warn("Module 2 demos — need Ollama or an OpenAI API key to run agents")
        info("Module 2 setup guide: docs/CREWAI_SETUP.md")

    if results.get("docker"):
        ok("Docker path — ready")
    else:
        info("Docker path — Docker Desktop not detected (Python path still works)")

    divider()
    print(f"\n{BOLD}Next step:{RESET}")
    if results.get("modules_1_3"):
        print("  Run the app:  streamlit run Home.py")
        print("  Then open:    http://localhost:8501\n")
    else:
        print("  Install core libraries first:  pip install -r requirements.txt\n")


def main():
    print(f"\n{BOLD}{'=' * 55}{RESET}")
    print(f"{BOLD}  AgenticAI Foundry — Environment Check{RESET}")
    print(f"{BOLD}  MIT Professional Education{RESET}")
    print(f"{BOLD}{'=' * 55}{RESET}")

    results = {}

    check_python()

    # Capture library results for summary
    core_libs = ["streamlit", "plotly", "pandas", "numpy", "tiktoken"]
    results["modules_1_3"] = all(
        importlib.util.find_spec(lib) is not None for lib in core_libs
    )
    check_libraries()

    check_docker()
    try:
        result = subprocess.run(["docker", "info"], capture_output=True, timeout=10)
        results["docker"] = result.returncode == 0
    except Exception:
        results["docker"] = False

    check_ollama()

    # Simple Ollama check for summary
    import urllib.request
    try:
        urllib.request.urlopen("http://localhost:11434/api/tags", timeout=2)
        results["module_2_ollama"] = True
    except Exception:
        results["module_2_ollama"] = False

    check_openai()
    results["module_2_openai"] = bool(
        os.environ.get("OPENAI_API_KEY", "").startswith("sk-")
    )

    summary(results)


if __name__ == "__main__":
    main()
