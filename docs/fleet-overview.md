# ALC Fleet Overview — 2026-09-12

## ALC Business Agent Fleet

| Agent | Functional Name | Host | Endpoint | LLM | Role | Status |
|---|---|---|---|---|---|---|
| Converter | Converter | X-Mansion (.65) | hermes-converter:9900 | GPT-Astra | CRM/Conversion/Delivery | Active |
| Researcher | Researcher | X-Mansion (.65) | hermes-researcher:9900 | Grok | Prospect/Discovery/Marketing | Active |
| Scout | Scout | Danger Room (.84) | 192.168.4.84:9900 | qwen3:20b | Prospect (local CPU) | PARKED |
| Builder | Builder | Danger Room (.80) | 192.168.4.80:9900 | — | Delivery (local GPU) | PARKED |

## Orchestration Layer (ai-council repo)

| Agent | Functional Name | Host | Endpoint | LLM | Role |
|---|---|---|---|---|---|
| Orchestrator | Orchestrator | X-Mansion (.65) | hermes-orchestrator:9900 | Claude Sonnet 4.6 | Orchestration |
| Infrastructure | Infrastructure | X-Mansion (.65) | hermes-infrastructure:9900 | Claude Sonnet 4.6 | Infra |

## Danger Room Hardware
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
