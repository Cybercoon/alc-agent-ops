#!/usr/bin/env python3
"""Non-network hygiene tests for alc-agent-ops docs (Phase 1)."""
from pathlib import Path
import sys
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REQUIRED = [
    "README.md",
    "lessons-learned.md",
    "architect-phase1-readiness.md",
    "phase-1-plan.md",
    "blockers-log.md",
]
SECRETISH = re.compile(
    r"(ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|Bearer [A-Za-z0-9._-]{20,})",
    re.I,
)


def main() -> int:
    failed = 0
    for name in REQUIRED:
        path = DOCS / name
        if not path.is_file():
            print(f"FAIL missing {path}")
            failed += 1
            continue
        text = path.read_text(encoding="utf-8")
        if len(text.strip()) < 40:
            print(f"FAIL too short {path}")
            failed += 1
        if SECRETISH.search(text):
            print(f"FAIL secret-like token in {path}")
            failed += 1
        else:
            print(f"OK {path.relative_to(ROOT)} ({len(text)} bytes)")
    readme = (DOCS / "README.md").read_text(encoding="utf-8")
    if "architect-phase1-readiness.md" not in readme:
        print("FAIL docs/README.md does not index architect-phase1-readiness.md")
        failed += 1
    else:
        print("OK docs/README.md indexes architect-phase1-readiness.md")
    if failed:
        print(f"FAILED {failed}")
        return 1
    print("PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
