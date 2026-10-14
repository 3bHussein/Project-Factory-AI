# Local Project Factory AI worker setup (Windows)
# Installs no paid APIs and does not start generation automatically.
$ErrorActionPreference = "Stop"
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw "Python 3.11+ is required. Install Python first."
}
if (-not (Get-Command ollama -ErrorAction SilentlyContinue)) {
    Write-Host "Ollama is not installed. Install from https://ollama.com/download and rerun."
    exit 1
}
Write-Host "Python:" (python --version)
Write-Host "Ollama:" (ollama --version)
Write-Host "Downloading local coding model (requires disk space and internet)..."
ollama pull qwen2.5-coder:7b
if ($LASTEXITCODE -ne 0) { throw "Model download failed." }
Write-Host "Ready. Run 'ollama serve' in a separate terminal if not running."
Write-Host "Use: python scripts/local_ollama_agent.py requests/YOUR-ISSUE.job.json"
Write-Host "Then review output before running with --write."
