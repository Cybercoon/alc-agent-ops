# Infra Map

## Hosts

| Host | IP | Role | OS |
|---|---|---|---|
| X-Mansion | 192.168.4.65 | Primary agent host | Ubuntu / Docker |
| Danger Room | 192.168.4.80 | GPU inference (ironman) | Ubuntu / Ollama |
| Danger Room | 192.168.4.84 | CPU inference (batman) | Ubuntu / Ollama |
| MSI Laptop | 192.168.4.x | Dev / fallback | Windows 11 |

## X-Mansion Containers (alc-hermes-x-mansion stack)

| Container | Functional Name | A2A Port | MCP Port | LLM Provider |
|---|---|---|---|---|
| hermes-orchestrator | Orchestrator | 18701 | 18711 | anthropic (Claude Sonnet 4.6) |
| hermes-converter | Converter | 18702 | 18712 | openai (GPT-Astra) |
| hermes-researcher | Researcher | 18703 | 18713 | xai-oauth (Grok) |
| hermes-infrastructure | Infrastructure | 18704 | 18714 | anthropic (Claude Sonnet 4.6) |

Compose file: `/home/batman/hermes-six-agent/deploy/x-mansion/compose.yaml`
Stack name: `alc-hermes-x-mansion`
Image: `nousresearch/claude-code:latest`

## Shared Filesystem
- Mount: `/opt/data/shared/` (all X-Mansion containers)
- Heartbeat check: `/opt/data/shared/heartbeat.txt`

## Mem0
- Host: `http://192.168.4.65:8765`
- Namespaces: `council`, `alc-fleet`
- Status: 401 issue pending (I-3)

## Danger Room Hardware
- **192.168.4.80 (ironman)** — RTX 3060 Ti (8GB) + RTX A2000 (6GB) = 14GB VRAM | 30GB RAM | Ollama v0.33.1
- **192.168.4.84 (batman)** — CPU inference | Ollama

## SSH Access
- Infrastructure keypair: `/opt/data/.ssh/id_ed25519_architect`
- Authorized on: `ironman@192.168.4.80`, `ironman@192.168.4.84`
- X-Mansion batman-host: via A2A/curl only (not SSH)
