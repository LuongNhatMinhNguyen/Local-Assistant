# Local-Assistant

A modular personal assistant for day-to-day tasks, built as a data engineering / data science portfolio project.
Approach: plain, well-typed Python modules first; a local LLM (e.g. via Ollama) is added later as a router that maps natural language to module actions.

## How AI assistance is used in this project

All code in this repository is written by me. Claude is used as a mentor and reviewer, not a code generator:

- Explain concepts, trade-offs, and design options before I implement.
- Review my code for bugs, edge cases, and style; point out issues clearly.
- Help read errors and debug, but let me write the fix.
- Do not generate full implementations. Short syntax examples are fine when asked.

## Project layout

```
local-assistant/            ← Python package; run commands from here
  log.py                    ← CLI entry point: records a media entry
  data/database.py          ← DuckDB connection and table setup (data/assistant.db)
  modules/
    analytics_pipeline/     ← media log module (games, films, manga, books)
      collector.py          ← builds the raw entry with a UTC timestamp
      transformer.py        ← cleans and normalizes fields
      loader.py             ← inserts into DuckDB table media_logs
      schema.py             ← pydantic models (in progress)
      analysis.py           ← pandas summaries (planned)
      dashboard.py          ← Streamlit dashboard (planned)
```

## Stack

Python · pydantic · DuckDB · pandas · Streamlit · FastAPI/uvicorn · pytest
Run: `cd local-assistant && python log.py`

## Architecture

- Each feature is a self-contained module under `modules/`.
- Data flows through an ETL-style pipeline: collect → transform (validate) → load.
- Every module will expose the same contract (name, supported actions, typed pydantic request/response), so a router can call any module without knowing its internals. The router starts as a CLI parser and is later replaced by an LLM using tool calling; modules do not change.

## Conventions

- Type hints on all functions; pydantic models for data passed between steps (no loose dicts).
- Timestamps stored in UTC.
- One module = one folder; no cross-module imports except via `data/` and shared core code.
- Tests in `tests/`, mirroring the module structure.

## Roadmap

1. [ ] `MediaEntry` pydantic model; pipeline passes models instead of dicts
2. [ ] Initialize the database on startup so a fresh clone runs
3. [ ] `requirements.txt` in UTF-8, add pandas
4. [ ] `analysis.py`: summaries (entries per category, activity over time)
5. [ ] `dashboard.py`: Streamlit view
6. [ ] pytest tests per module
7. [ ] Shared module contract + simple router
8. [ ] More modules: expenses, job applications, gym log
9. [ ] LLM router via local model; Docker; README
