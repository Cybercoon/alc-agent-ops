# ALC Agent Ops

Private repository for the ALC AI infrastructure. Serves two distinct ecosystems.

## Structure

```
alc-agent-ops/
  /council/          ← AI Council of Agents (meta-layer: builds + governs infrastructure)
  /alc-fleet/        ← ALC/Sisu business agents (purpose-built for business functions)
  /docs/             ← Shared wiki serving both ecosystems
  /scripts/          ← Shared utility scripts (health checks, relay, A2A tools)
```

## Ecosystems

### AI Council of Agents
Builds and governs the infrastructure. Does not operate within it.
- **Professor X (PX)** — Orchestration
- **Architect** — Infra implementation

### ALC/Sisu Agent Fleet
Executes business functions for ALC and Sisu.
- **Beast** — CRM / Delivery
- **Wolverine** — Prospect / Marketing
- **Magneto** — Parked
- **Forge** — Parked

## Quick Links
- [Fleet Overview](docs/fleet-overview.md)
- [Two-Ecosystem Model](docs/two-ecosystem-model.md)
- [Phase 1 Plan](docs/phase-1-plan.md)
- [Infra Map](docs/infra-map.md)
- [Blockers Log](docs/blockers-log.md)

## Usage

See `/docs/README.md` for full documentation index.

**Sensitive data (credentials, .env files, bearer tokens) never go in this repo.** See `.gitignore`.
