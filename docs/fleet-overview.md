# ALC Fleet Overview — 2026-09-12

## AI Council of Agents
| Agent | Host | Endpoint | LLM | Role |
|---|---|---|---|---|
| Professor X (PX) | X-Mansion (.65) | hermes-professor-x:9900 | Claude Sonnet 4.6 | Orchestration |
| Architect | X-Mansion (.65) | hermes-architect:9900 | Claude Sonnet 4.6 | Infra |

## ALC Fleet Agents
| Agent | Host | Endpoint | LLM | Role | Status |
|---|---|---|---|---|---|
| Beast | X-Mansion (.65) | hermes-beast:9900 | GPT-Astra | CRM/Convert/Delivery | Active |
| Wolverine | X-Mansion (.65) | hermes-wolverine:9900 | Grok | Prospect/Discovery/Marketing | Active |
| Magneto | Danger Room (.84) | 192.168.4.84:9900 | qwen3:20b | Prospect | PARKED |
| Forge | Danger Room (.80) | 192.168.4.80:9900 | — | Delivery | PARKED |

## Danger Room Hardware
Host: 192.168.4.80 | GPU: RTX 3060 Ti (8GB) + RTX A2000 (6GB) = 14GB VRAM | RAM: 30GB | Ollama: v0.33.1

## Phase 1 Infra Status
| # | Task | Status |
|---|---|---|
| I-1 | Shared filesystem | ✅ Complete |
| I-2 | Config preamble injection (Option B) | In progress |
| I-3 | Fix Mem0 401 on 192.168.4.65:8765 | Queued |
| I-4 | Mem0 persistent memory (Option C) | Phase 1 required |
| I-5 | GitHub repo | In progress |
| I-6 | Wiki seed | In progress |
