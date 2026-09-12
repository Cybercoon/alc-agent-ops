# ALC Agent Ops

Private repository for Advantage Leadership Consulting (ALC) AI agent operations.

This repo covers the **business agent fleet** — agents purpose-built to execute ALC business functions. Governance and orchestration infrastructure lives in the separate `ai-council` repo.

## Structure

```
alc-agent-ops/
  /docs/             ← Shared wiki: fleet overview, plans, ICP, infra map
  /configs/          ← Agent config.yaml files (one per agent)
  /compose/          ← Docker compose files for X-Mansion and other hosts
  /plans/            ← Versioned plan documents (v6.2, v6.3, v6.4, v6.5)
  /scripts/          ← Utility scripts (health checks, relay, A2A tools)
```

## ALC Agent Fleet

Executes business functions for Advantage Leadership Consulting (ALC).

| Agent | Functional Name | Role | Status |
|---|---|---|---|
| Converter | Converter | CRM / Conversion / Delivery | Active |
| Researcher | Researcher | Prospect / Discovery / Marketing | Active |
| Scout | Scout | Prospect (local CPU) | PARKED |
| Builder | Builder | Delivery (local GPU) | PARKED |

## AI Council of Agents

Governance and orchestration layer. See the [ai-council repository](https://github.com/Cybercoon/ai-council).

## Governance & Orchestration

The orchestration layer (Orchestrator + Infrastructure agents) is documented in the `ai-council` repo.

## Quick Links
- [Fleet Overview](docs/fleet-overview.md)
- [Phase 1 Plan](docs/phase-1-plan.md)
- [Infra Map](docs/infra-map.md)
- [ICP Definition](docs/icp-definition.md)
- [Blockers Log](docs/blockers-log.md)

## Usage

See `/docs/README.md` for full documentation index.

**Sensitive data (credentials, .env files, bearer tokens) never go in this repo.** See `.gitignore`.
