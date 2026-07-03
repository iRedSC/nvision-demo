#!/usr/bin/env python3
"""Seed the nvision demo Lovelace dashboard into HA storage on first boot."""

from __future__ import annotations

import json
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - HA container includes PyYAML
    yaml = None

STORAGE_DIR = Path("/config/.storage")
DASHBOARD_YAML = Path("/bootstrap/ui-lovelace.yaml")
DASHBOARD_ID = "nvision_demo"
DASHBOARD_KEY = f"lovelace.{DASHBOARD_ID}"
DASHBOARD_ENTRY = {
    "id": DASHBOARD_ID,
    "show_in_sidebar": True,
    "icon": "mdi:view-dashboard",
    "title": "nvision Demo",
    "require_admin": False,
    "mode": "storage",
    "url_path": "nvision-demo",
}


def load_views_config() -> dict:
    if yaml is None:
        raise RuntimeError("PyYAML is required to seed the demo dashboard")

    raw = yaml.safe_load(DASHBOARD_YAML.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or "views" not in raw:
        raise ValueError("ui-lovelace.yaml must contain a top-level views key")

    return raw


def write_dashboard_config(config: dict) -> None:
    dashboard_file = STORAGE_DIR / DASHBOARD_KEY
    if dashboard_file.exists():
        return

    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "version": 1,
        "minor_version": 1,
        "key": DASHBOARD_KEY,
        "data": {"config": config},
    }
    dashboard_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def register_dashboard() -> None:
    dashboards_file = STORAGE_DIR / "lovelace_dashboards"

    if dashboards_file.exists():
        store = json.loads(dashboards_file.read_text(encoding="utf-8"))
        items = store.setdefault("data", {}).setdefault("items", [])
        if any(item.get("id") == DASHBOARD_ID for item in items):
            return
        items.append(DASHBOARD_ENTRY)
    else:
        store = {
            "version": 1,
            "minor_version": 1,
            "key": "lovelace_dashboards",
            "data": {"items": [DASHBOARD_ENTRY]},
        }

    dashboards_file.write_text(json.dumps(store, indent=2), encoding="utf-8")


def main() -> None:
    if not DASHBOARD_YAML.exists():
        return

    config = load_views_config()
    write_dashboard_config(config)
    register_dashboard()


if __name__ == "__main__":
    main()
