# Phase 1 Plan

## Objectives
Bring the ALC / Sisu Coaching & Consulting agent fleet to operational readiness for business use.

## Infra Checklist

| ID | Task | Owner | Status | Notes |
|---|---|---|---|---|
| I-1 | Shared filesystem `/opt/data/shared/` | Infrastructure | ✅ Complete | Mounted and verified |
| I-2 | Config preamble injection (Option B) | Infrastructure | In progress | Fleet-wide system prompt consistency |
| I-3 | Fix Mem0 401 on 192.168.4.65:8765 | Infrastructure | Queued | Auth mismatch on local Mem0 |
| I-4 | Mem0 persistent memory (Option C) | Infrastructure | Phase 1 required | Two namespaces: council / alc-fleet |
| I-5 | GitHub repo `alc-agent-ops` | Infrastructure | ✅ Complete | Live on GitHub |
| I-6 | Wiki seed | Infrastructure | ✅ Complete | All docs seeded |

## Phase 1 Gate Criteria
- [ ] All agents reachable via A2A
- [ ] Shared filesystem mounted and readable by all containers
- [ ] Mem0 operational (no 401s)
- [ ] GitHub repos live (alc-agent-ops + ai-council)
- [ ] Converter (Beast) HubSpot integration verified post-recreate
- [ ] Config preamble injected to all active agents

## Out of Scope (Phase 2+)
- Scout (Magneto) and Builder (Forge) reactivation
- n8n workflow automation
- ICP ML pipeline
