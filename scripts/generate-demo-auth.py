#!/usr/bin/env python3
"""Write demo auto-login config from environment variables."""

from __future__ import annotations

import json
import os
from pathlib import Path

OUTPUT = Path("/config/www/demo/config.js")
BOOTSTRAP_DEMO = Path("/bootstrap/www/demo")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    for name in ("index.html", "auto-login.js"):
        source = BOOTSTRAP_DEMO / name
        if source.exists():
            (OUTPUT.parent / name).write_text(
                source.read_text(encoding="utf-8"),
                encoding="utf-8",
            )

    payload = {
        "username": os.environ.get("DEMO_USERNAME", "").strip(),
        "password": os.environ.get("DEMO_PASSWORD", "").strip(),
        "dashboard": os.environ.get("DEMO_DASHBOARD_PATH", "/lovelace/nvision-demo").strip(),
    }
    OUTPUT.write_text(
        f"window.DEMO_AUTH = {json.dumps(payload)};\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
