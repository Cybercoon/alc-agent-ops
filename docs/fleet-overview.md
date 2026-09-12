# ALC Fleet Overview — 2026-09-12

## ALC Business Agent Fleet

| Agent | Functional Name | Host | Endpoint | LLM | Role | Status |
|---|---|---|---|---|---|---|
| Orchestrator | Orchestrator | AsteroidM (192.168.4.80) | 192.168.4.80:9900 | Claude Sonnet 4.6 | Orchestration | Active |
| Converter | Converter | AsteroidM (192.168.4.80) | 192.168.4.80:9901 | GPT-Astra | CRM/Conversion/Delivery | Active |
| Researcher | Researcher | AsteroidM (192.168.4.80) | 192.168.4.80:9902 | Grok | Prospect/Discovery/Marketing | Active |
| Scout | Scout | AsteroidM (192.168.4.80) | 192.168.4.80:9903 | qwen3:14b | Prospect (local CPU) | PARKED |
| Builder | Builder | AsteroidM (192.168.4.80) | 192.168.4.80:9904 | — | Delivery (local GPU) | PARKED |
| Infrastructure | Infrastructure | AsteroidM (192.168.4.80) | 192.168.4.80:9905 | Claude Sonnet 4.6 | Infra | Active |

> **AsteroidM** = Danger Room server (192.168.4.80) — production hosting for all ALC fleet agents.
> **X-Mansion** = development / backup environment only (not production hosting).

## Orchestration Layer (ai-council repo)

See [https://github.com/Cybercoon/ai-council](https://github.com/Cybercoon/ai-council) for governance and orchestration documentation.

## AsteroidM Hardware
Host: 192.168.4.80 | GPU: RTX 3060 Ti (8GB) + RTX A2000 (6GB) = 14GB VRAM | RAM: 30GB | Ollama: v0.33.1

## Phase 1 Infra Status
| # | Task | Status |
|---|---|---|
| I-1 | Shared filesystem | ✅ Complete |
| I-2 | Config preamble injection (Option B) | In progress |
| I-3 | Fix Mem0 401 on 192.168.4.65:8765 | Queued |
| I-4 | Mem0 persistent memory (Option C) | Phase 1 required |
| I-5 | GitHub repo | ✅ Complete |
| I-6 | Wiki seed | ✅ Complete |
