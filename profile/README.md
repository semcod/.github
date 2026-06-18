# Semcod

[![Organization](https://img.shields.io/badge/GitHub-semcod-black.svg)](https://github.com/semcod)
[![Projects](https://img.shields.io/badge/projects-68-blue.svg)](https://github.com/semcod?tab=repositories)
[![Language](https://img.shields.io/badge/primary-Python-3776AB.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Ekosystem open-source do semantycznej optymalizacji kodu — analiza, jakość, automatyzacja LLM, orchestracja i delivery.

---

## Projekty

### Code Analysis & Flow

| Projekt | Opis | Język |
|---------|------|-------|
| [code2docs](https://semcod.github.io/code2docs/) | Auto-generate and sync README, API docs and architecture diagrams from code2llm analysis. | Python |
| [code2llm](https://semcod.github.io/code2llm/) | Python static analysis for CFG, DFG, call graphs and TOON output — LLM-ready code flow intelligence. | Python |
| [code2logic](https://semcod.github.io/code2logic/) | Natural-language code understanding on top of code2llm — query codebases with NLP and semantic flow analysis. | Python |
| [code2schema](https://semcod.github.io/code2schema/) | Extract JSON Schema and OpenAPI from Python code structure. | HTML |
| [codot](https://semcod.github.io/codot/) | Graphviz DOT generator for architecture diagrams from code2llm analysis. | HTML |
| [intract](https://semcod.github.io/intract/) | Intent-contract layer for code, APIs, CI/CD and DevOps artifacts — describe, validate and monitor intent across the stack. | HTML |
| [nexu](https://semcod.github.io/nexu/) | Visual intent-contract orchestrator — freeze project slices, evolve capsules, verify delivery intent. | Python |
| [redup](https://semcod.github.io/redup/) | AST-level duplication detector and refactor planner that feeds LLM-driven deduplication workflows. | HTML |
| [regix](https://semcod.github.io/regix/) | Regression index — measure and alert on code-quality regressions between git versions. | Python |
| [vallm](https://semcod.github.io/vallm/) | Validate LLM-generated code in sandboxed environments before merge — syntax, tests, security and intent checks. | HTML |

### Quality Gates & Linting

| Projekt | Opis | Język |
|---------|------|-------|
| [prefact](https://semcod.github.io/prefact/) | Python code quality tool with LLM-aware rules, plugins and enterprise lint features. | Python |
| [pyqual](https://semcod.github.io/pyqual/) | Declarative quality-gate loops for AI-assisted development — ruff, mypy, bandit and custom gates in one CLI. | Python |
| [pyqual-demo](https://semcod.github.io/pyqual-demo/) | Demo fixtures and examples for pyqual quality-gate configurations. | HTML |
| [qualbench](https://semcod.github.io/qualbench/) | CI benchmark for AI-generated code — measures production readiness, not just correctness. | Python |
| [redsl](https://semcod.github.io/redsl/) | ReDSL — LLM-powered autonomous refactoring with self-learning DSL actions. | Python |
| [weekly](https://semcod.github.io/weekly/) | Weekly project health analyzer — code quality, dependencies, tests and actionable improvement reports. | Python |

### LLM Routing & Preprocessing

| Projekt | Opis | Język |
|---------|------|-------|
| [algitex](https://semcod.github.io/algitex/) | Progressive algorithmization toolchain — from LLM prompts to deterministic code, proxy and tickets. | Python |
| [costs](https://semcod.github.io/costs/) | Track AI usage costs per git commit and model with liteLLM integration — zero-config spend analytics. | HTML |
| [env2llm](https://semcod.github.io/env2llm/) | Map runtime environment (services, artifacts, env vars) into LLM-friendly context for agent decisions. | HTML |
| [llx](https://semcod.github.io/llx/) | Intelligent LLM model router driven by real code metrics — successor to preLLM. | Python |
| [prellm](https://semcod.github.io/prellm/) | Small-then-large LLM preprocessing layer — like litellm.completion() with a smart routing preprocessor. | Python |
| [proxym](https://semcod.github.io/proxym/) | AI proxy with semantic cache, delta context buffers and ticket routing for semcod toolchains. | Python |

### Automation & Orchestration

| Projekt | Opis | Język |
|---------|------|-------|
| [koru](https://semcod.github.io/koru/) | Meta-orchestrator for closed-loop refactor automation across IDEs and semcod repos — detect, plan, execute, verify, heal, repeat. | Python |
| [nxdo](https://semcod.github.io/nxdo/) | Generate the next 10 project tasks from repo state, git history and an LLM prompt. | HTML |
| [planfile](https://semcod.github.io/planfile/) | SDLC automation platform with tickets, sprints, CI/CD integration and autonomous bug-fix loops. | Python |
| [regres](https://semcod.github.io/regres/) | Regression test orchestration for multi-service semcod workspaces. | Python |
| [reko](https://semcod.github.io/reko/) | Refactor hardcoded values, structures and patterns in Python projects with LLM-assisted extraction. | HTML |
| [repatch](https://semcod.github.io/repatch/) | Generate and apply config patches from natural language intent across semcod projects. | HTML |
| [swop](https://semcod.github.io/swop/) | Software workspace orchestration platform — DOQL specs, graphs and refactor pipelines. | Python |
| [taskill](https://semcod.github.io/taskill/) | Kill runaway dev processes and clean zombie tasks from local agent sessions. | Python |
| [taskinity](https://semcod.github.io/taskinity/) | Task affinity scheduler for parallel semcod automation workers. | HTML |
| [wup](https://semcod.github.io/wup/) | What's Up — intelligent file watcher that runs regression tests and visual diffs on code changes. | Python |

### IDE & Control Planes

| Projekt | Opis | Język |
|---------|------|-------|
| [gillm](https://semcod.github.io/gillm/) | GUI control plane with NLP and intent contracts — automate desktop apps via DSL, MCP and REST. | HTML |
| [hillm](https://semcod.github.io/hillm/) | Hardware interface LLM — control displays, cameras, audio, USB, serial, Modbus and more. | Python |
| [imgl](https://semcod.github.io/imgl/) | Image-to-layout — screenshot OCR and semantic UI reconstruction for GUI test automation. | Python |
| [nlp2env](https://semcod.github.io/nlp2env/) | MCP server for reading and writing .env variables (SMTP, API keys and custom secrets). | Python |
| [nlp2uri](https://semcod.github.io/nlp2uri/) | Resolve natural language to local URIs and execute cross-platform desktop or IDE actions. | Python |
| [skillm](https://semcod.github.io/skillm/) | Universal skill registry — reuse Python, Docker, CLI and REST capabilities via MCP. | Python |
| [tillm](https://semcod.github.io/tillm/) | Text-interface LLM control plane for shell automation — pair with gillm for GUI+CLI agent control. | HTML |

### DevOps & Release

| Projekt | Opis | Język |
|---------|------|-------|
| [dbos](https://semcod.github.io/dbos/) | Database operations toolkit — migrations, health checks and backup automation. | HTML |
| [giton](https://semcod.github.io/giton/) | Git onboarding assistant — init repos, remotes, hooks and semcod workflow templates. | HTML |
| [goal](https://semcod.github.io/goal/) | pip install goal — automated git push with smart conventional commits, changelog updates, version tagging, and interactive or headless… | Python |
| [mcp](https://semcod.github.io/mcp/) | Shared MCP server templates and adapters for the semcod ecosystem. | Python |
| [metrun](https://semcod.github.io/metrun/) | Performance profiling with bottleneck detection and regression tracking for Python services. | Python |
| [op3](https://semcod.github.io/op3/) | Operations orchestration POC — probes, migrations and kiosk deployment recipes. | Python |
| [protos](https://semcod.github.io/protos/) | Migration platform for extracting bounded slices from legacy systems into protobuf services. | Python |
| [resplit](https://semcod.github.io/resplit/) | Historical deployment analysis — walk git history, deploy per commit, test endpoints and restore working fragments. | Python |
| [tagi](https://semcod.github.io/tagi/) | Auto-tag git commits and releases with semantic version and conventional-commit metadata. | Python |

### Documentation & Markdown

| Projekt | Opis | Język |
|---------|------|-------|
| [clickmd](https://semcod.github.io/clickmd/) | Markdown rendering for CLI apps with syntax highlighting, tables and rich terminal output. | HTML |
| [docval](https://semcod.github.io/docval/) | Validate documentation claims against runnable commands and code references. | Python |
| [domd](https://semcod.github.io/domd/) | Do Markdown Docs — detect, run and document working commands in DONE.md and failures in TODO.md. | Python |
| [mdflow](https://semcod.github.io/mdflow/) | Markdown document workflow engine with lint, link check and publish pipelines. | HTML |
| [sumd](https://semcod.github.io/sumd/) | Generate SUMD operational descriptors from code for LLM agents and automation pipelines. | Python |
| [todocs](https://semcod.github.io/todocs/) | Convert project docs to unified markdown sites from scattered README fragments. | Python |

### Testing & Benchmarks

| Projekt | Opis | Język |
|---------|------|-------|
| [ats-benchmark](https://semcod.github.io/ats-benchmark/) | Benchmark LLM context compression — code2logic vs nfo vs raw code baselines. | Python |
| [deta](https://semcod.github.io/deta/) | Deterministic test artifact generator for reproducible QA fixtures. | Python |
| [testless](https://semcod.github.io/testless/) | Reduce test boilerplate by inferring test cases from code structure and intent contracts. | Python |

### System Repair & Self-Healing

| Projekt | Opis | Język |
|---------|------|-------|
| [fixop](https://semcod.github.io/fixop/) | Fix operations playbook runner for recurring infra and dev environment issues. | HTML |
| [fixos](https://semcod.github.io/fixos/) | AI diagnostics and repair for Fedora/Linux and Windows — audio, thumbnails, Lenovo Yoga hardware and system issues. | Python |
| [heal](https://semcod.github.io/heal/) | Experimental shell-error fixer using LLM assistance for command-line workflows. | Python |
| [pactfix](https://semcod.github.io/pactfix/) | Real-time Bash script analyzer and auto-fixer with ShellCheck integration. | Python |
| [pfix](https://semcod.github.io/pfix/) | Self-healing Python runtime — catch errors, patch code and dependencies via LLM and MCP. | Python |

### Observability & Logging

| Projekt | Opis | Język |
|---------|------|-------|
| [nfo](https://semcod.github.io/nfo/) | Automatic function logging via decorators — SQLite, CSV, Markdown, JSON, Prometheus and chat alerts. | Python |

### Frameworks & DSL

| Projekt | Opis | Język |
|---------|------|-------|
| [toonic](https://semcod.github.io/toonic/) | TOON file format platform for LLM-optimized typed logic representation of models, functions and CI/CD. | Python |

### Platform & SaaS

| Projekt | Opis | Język |
|---------|------|-------|
| [godot](https://semcod.github.io/godot/) | Godot game engine integration utilities for semcod automation demos. | HTML |
| [semcod](https://semcod.github.io/semcod/) | Semcod organization meta-package and shared tooling for the semantic code optimization ecosystem. | Python |
| [wupbro](https://semcod.github.io/wupbro/) | Browser-side companion for WUP visual regression and endpoint probing. | HTML |
| [www](https://semcod.github.io/www/) | Semcod SaaS platform — one-click code audit, PR comment bot, health badges, MCP and marketplace auto-fix. | Python |

---

## Statystyki

- **Łącznie projektów**: 68
- **Projekty Python**: 47
- **Strony projektów**: `https://semcod.github.io/<repo>/`

## Quick Start

```bash
git clone https://github.com/semcod/<project-name>.git
pip install <project-name>
```

_Ostatnia aktualizacja: 2026-06-18_
