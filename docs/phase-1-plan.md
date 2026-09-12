# Phase 1 Plan

## Objectives
Bring the ALC agent fleet to operational readiness for business use.

## Infra Checklist

| ID | Task | Owner | Status | Notes |
|---|---|---|---|---|
| I-1 | Shared filesystem `/opt/data/shared/` | Architect | ✅ Complete | Mounted and verified |
| I-2 | Config preamble injection (Option B) | Architect | In progress | Fleet-wide system prompt consistency |
| I-3 | Fix Mem0 401 on 192.168.4.65:8765 | Architect | Queued | Auth mismatch on local Mem0 |
| I-4 | Mem0 persistent memory (Option C) | Architect | Phase 1 required | Two namespaces: council / alc-fleet |
| I-5 | GitHub repo `alc-agent-ops` | Architect | In progress | Local build complete; needs GitHub PAT |
| I-6 | Wiki seed | Architect | In progress | Depends on I-5 |

## Phase 1 Gate Criteria
- [ ] All agents reachable via A2A
- [ ] Shared filesystem mounted and readable by all containers
- [ ] Mem0 operational (no 401s)
- [ ] GitHub repo live with initial wiki
- [ ] Beast HubSpot integration verified post-recreate
- [ ] Config preamble injected to all active agents

## Out of Scope (Phase 2+)
- Magneto and Forge reactivation
- n8n workflow automation
- ICP ML pipeline
