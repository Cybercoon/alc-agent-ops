# Lessons Learned

Cross-build lessons shared between AI Council and ALC Fleet. Every infrastructure build must contribute here.

## Infrastructure

### L-001 — ironman hardening kills Hermes (2026-09)
**Context:** Attempted to apply ironman Docker hardening template to X-Mansion containers.
**Lesson:** `init: true` + `cap_drop: ALL` + `no-new-privileges: true` kills Hermes UID drop → exit 111.
**Rule:** Never apply ironman hardening to X-Mansion Hermes containers. Patch compose surgically only.

### L-002 — HubSpot API key not persistent across container recreates (2026-09)
**Context:** Converter container recreated; HubSpot integration broke.
**Lesson:** API key not persisted in compose env — lost on recreate.
**Rule:** After every Converter recreate, re-write key to `/home/batman/hermes-six-agent/data/beast/.env` and verify via A2A read-only test. Do not assume prior READY=yes holds.

### L-003 — YAML dump silently drops scalar keys (2026-09)
**Context:** Restoring Scout mem0/A2A toolset config via yaml.dump.
**Lesson:** `yaml.dump` silently drops scalar keys. Config appears valid but tools are missing.
**Rule:** Never yaml.dump a config back. Use restore-from-backup + targeted text patch + yaml.safe_load validate before restart.

### L-004 — Mem0 toolset wiring requires BOTH platform and builtin entries (2026-09)
**Context:** Scout mem0 tools appeared wired but were empty at runtime.
**Lesson:** Both `platform_toolsets.a2a` AND `known_builtin_toolsets.a2a` must list `[memory, session_search]`.
**Rule:** Check both locations when debugging missing Mem0 tools.

### L-005 — Shared FS verified via heartbeat file, not mount check alone (2026-09-12)
**Context:** I-1 shared filesystem verification.
**Lesson:** A directory existing doesn't prove cross-container visibility. Write a heartbeat file; peer agents read it.
**Rule:** Heartbeat pattern: writer writes to `/opt/data/shared/heartbeat.txt`, peer reads it to confirm mount.

## Auth & Credentials

### L-006 — Provider auth lives in auth.json, not .env (2026-09)
**Context:** Peers checking .env for Anthropic tokens.
**Lesson:** Claude/Anthropic OAuth lives in `/opt/data/auth.json`. `.env` holds service keys (HubSpot, Mem0, A2A bearer).
**Rule:** When diagnosing auth failures, check the right file for the right credential type.

### L-007 — Telegram masks credentials in both directions (2026-09)
**Context:** Attempting to relay API keys via Telegram chat.
**Lesson:** Keys sent through Telegram are redacted as '***' — unreliable channel for credentials.
**Rule:** Adam must type credentials manually at the terminal. Never relay secrets through Telegram chat.

### L-008 — gpt-5-mini is not a ChatGPT Codex seat (2026-09-15)
**Context:** Architect Phase 1 cutover to lower-reasoning ChatGPT. `config.yaml` was set to `openai-codex` / `gpt-5-mini`.
**Lesson:** ChatGPT Codex OAuth returns HTTP 400 `The 'gpt-5-mini' model is not supported when using Codex with a ChatGPT account.` Hermes then falls back to `xai-oauth` / `grok-4.6`, so the worker looks configured for ChatGPT while the live session is Grok. Live catalog on this account listed `gpt-6-astra`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5.5`.
**Rule:** For Architect’s ChatGPT implementation seat use an entitled Codex slug (`gpt-5.6-luna` as of 2026-09-15). Never claim ChatGPT-primary from `config.yaml` alone — confirm `agent.log` model/provider for the session. Do not assign `gpt-6-astra` to Architect (Orchestrator high-reasoning seat).
