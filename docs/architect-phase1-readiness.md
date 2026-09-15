# Architect Phase 1 readiness (ChatGPT implementation worker)

Date (UTC): 2026-09-15
Owner: Architect
Scope: Phase 1 only — make Architect ready as Orchestrator’s lower-reasoning ChatGPT implementation worker.
Non-goals honored: no worker-routing map change, no production deploy, no secret disclosure.

## Configured provider / model

- Intended primary: `openai-codex` / `gpt-5.6-luna`
- Codex backend: `https://chatgpt.com/backend-api/codex`
- OAuth pool entry (local): one credential, label `architect-chatgpt-lower`, id `94430d`, auth_type `oauth`
- Fallbacks (unchanged): `xai-oauth` / `grok-4.6`, then local `custom` / `gpt-oss:20b`
- ChatGPT plan claim on this OAuth JWT: `plus` (no secret material recorded here)

## Why not gpt-5-mini

`config.yaml` previously had `model.default: gpt-5-mini`. Live Codex catalog for this account does **not** include `gpt-5-mini`. Session `20260915_132406_9fe38621` attempted `openai-codex` / `gpt-5-mini` and received HTTP 400:

`The 'gpt-5-mini' model is not supported when using Codex with a ChatGPT account.`

Hermes then activated fallback `xai-oauth` / `grok-4.6` for that A2A session.

Visible Codex slugs on this account (GET `/backend-api/codex/models`, 2026-09-15):

- `gpt-6-astra` (high-reasoning — leave for Orchestrator)
- `gpt-5.6-sol`
- `gpt-5.6-terra`
- `gpt-5.6-luna` ← Architect lower seat
- `gpt-5.5`

CLI inference probes billed to `openai-codex` (not Grok):

| model | session_id | billing_provider |
|---|---|---|
| gpt-5.6-luna | 20260915_133833_5497ba | openai-codex |
| gpt-5.5 | 20260915_133851_f62cc6 | openai-codex |
| gpt-5.6-terra | 20260915_133909_81e3af | openai-codex |
| gpt-5-mini (negative) | 20260915_133112_75361b | xai-oauth (fallback) |

## OAuth isolation

- This container’s `credential_pool.openai-codex` holds **one** entry.
- This container cannot read Orchestrator’s `auth.json`, so same-account occupancy is **not independently proven**.
- The same token’s live catalog includes `gpt-6-astra`, which is Orchestrator’s high-reasoning slug. Treat as a remaining isolation question for Adam / Agent Trainer (1–2 agents per ChatGPT OAuth account).

## A2A reachability

| Check | Result |
|---|---|
| GET `http://127.0.0.1:9915/health` | 200 `{"status":"ok","agent":"Architect"}` |
| GET `http://hermes-architect:9915/health` | 200 same |
| GET `http://192.168.4.84:9915/health` | 200 same |
| GET `/.well-known/agent-card.json` | 200 name=Architect url=`http://192.168.4.84:9915/` |
| `message/send` no bearer | 401 JSON-RPC `-32050 unauthorized` |
| `message/send` bad bearer | 401 JSON-RPC `-32050 unauthorized` |
| `message/send` from `127.0.0.1` with valid bearer | 403 `-32052` peer not trusted (loopback not in `A2A_TRUSTED_PEERS`) |
| `tasks/get` + `GetTask` + `tasks/list` from `172.20.0.6` / `hermes-architect` with bearer | 200 |
| This Phase 1 handoff task | `task-ab7dd958cf234b28` context `ctx-4cd9a7eb6bba4ff9` (authenticated inbound `message/send`) |

Public A2A URL: `http://192.168.4.84:9915` (env `A2A_PUBLIC_URL`). Agent name: Architect. Port: 9915.

## GitHub / workspace

| Item | Status |
|---|---|
| Workspace | `/opt/data/alc-agent-ops` (`Cybercoon/alc-agent-ops`) |
| Secondary | `/opt/data/ai-council` (`Cybercoon/ai-council`) |
| Git identity | `Architect` / `architect@alc-agent-ops` |
| Token user | `Cybercoon`, scope `repo` |
| Repo permissions (both) | admin/maintain/push/triage/pull = true |
| `gh` CLI | not installed; PRs via git + GitHub HTTP API |
| Default policy | branch → tests → PR for Adam; no production deploy unless task + Adam authorize |

## Remaining blockers

1. **This A2A session stays on Grok** until a new session starts. Gateway restart from inside this process is blocked. New inbound A2A after this config write should pick up `gpt-5.6-luna`.
2. **ChatGPT account isolation vs Orchestrator** not verifiable from this container; catalog includes `gpt-6-astra`.
3. **`gh` missing** — PR workflow uses git push + GitHub API.
4. **No Docker daemon** in this container — cannot restart own gateway or other workers from here.
