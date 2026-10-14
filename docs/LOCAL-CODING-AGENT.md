# Local coding worker (opt-in, no paid API)

This is the first **actual model-backed code generator** in Project Factory AI. It uses a locally installed Ollama model; GitHub-hosted Actions cannot access your personal Ollama server by default.

## Requirements
- Python 3.11+
- [Ollama](https://ollama.com/) installed on your computer
- Enough memory to run the selected model
- A **reviewed** request specification and matching `*.job.json` manifest checked out locally

## Example

```bash
ollama pull qwen2.5-coder:7b
ollama serve
python scripts/local_ollama_agent.py requests/issue-42-task-m.job.json
python scripts/local_ollama_agent.py requests/issue-42-task-m.job.json --write
python scripts/agent_output_gate.py task-m
python -m unittest discover -s projects/task-m -p 'test_*.py'
```

The first run is dry-run. The second writes only into a previously nonexistent `projects/task-m` directory. Generated code is **untrusted**. Review it before running any tests, installing dependencies or creating a PR. There is no automatic GitHub push, no automatic merge, no cloud API and no secret handling. The model may fail to return valid JSON or generate working code; iterate manually until checks pass.

**Not yet autonomous:** A human must install Ollama, select a model, approve the specification, run the worker locally, review the generated files, and submit a PR. GitHub Pages cannot directly run this worker.
