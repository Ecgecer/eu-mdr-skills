#!/usr/bin/env python3
"""Fail if a generated portable artifact is stale.

The whole claim of this repo is that a reader can re-check every finding against
verbatim statute text. That breaks quietly if the Gemini/GPT copy drifts from the
Claude one -- someone using the bundle would be reviewing against an older rule
while the repo says otherwise, and nothing would show it.

Run in CI, and before publishing.
"""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
r = subprocess.run([sys.executable, str(ROOT / "scripts" / "build-portable.py"), "--check"],
                   capture_output=True, text=True)
print(r.stdout.rstrip())
if r.stderr.strip():
    print(r.stderr.rstrip(), file=sys.stderr)
sys.exit(r.returncode)
