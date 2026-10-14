#!/usr/bin/env bash
# Local setup only: no GitHub credentials, no cloud AI subscription.
set -euo pipefail
command -v python3 >/dev/null || { echo 'Python 3.11+ required'; exit 1; }
command -v ollama >/dev/null || { echo 'Install Ollama from https://ollama.com/download'; exit 1; }
python3 --version
ollama --version
ollama pull qwen2.5-coder:7b
printf '%s\n' 'Ready. Start ollama serve if needed, then use:' \
  'python3 scripts/local_ollama_agent.py requests/YOUR-ISSUE.job.json'
