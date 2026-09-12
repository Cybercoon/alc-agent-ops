# Blockers Log

Living document. Active blockers tracked here. Resolved blockers moved to bottom.

## Active Blockers

| work_id | Description | Blocker | Owner | Opened |
|---|---|---|---|---|
| I-3 | Mem0 401 on 192.168.4.65:8765 | Auth mismatch — API key in .env may not match Mem0 server config. Needs live test after key verification. | Infrastructure | 2026-09-12 |
| I-2 | Config preamble injection | In progress — needs per-agent testing | Infrastructure | 2026-09-12 |
| I-4 | Mem0 persistent memory | Depends on I-3 resolution | Infrastructure | 2026-09-12 |

## Resolved Blockers

| work_id | Description | Resolution | Closed |
|---|---|---|---|
| I-1 | Shared filesystem | Mounted and verified. Heartbeat written to /opt/data/shared/heartbeat.txt | 2026-09-12 |
| infra-github-repo-01 | GitHub repo creation | alc-agent-ops and ai-council repos created and pushed | 2026-09-12 |
