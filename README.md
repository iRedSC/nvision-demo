# nvision demo

Standalone Home Assistant demo for the nvision dashboard cards.

This repo is intentionally separate from [`iRedSC/nvision`](https://github.com/iRedSC/nvision). It owns only the public demo deployment: Docker Compose, Home Assistant demo configuration, and Lovelace dashboard YAML.

## Run Locally

```bash
cp .env.example .env
docker compose up -d
```

Open `http://localhost:8123`, complete Home Assistant onboarding, then open **nvision Demo** in the sidebar.

The demo loads the checked-in card bundle from `/local/nvision/nvision.js`. On first boot, the container seeds a **storage-mode** dashboard from `demo/home-assistant/ui-lovelace.yaml`, so you can edit it with the normal Lovelace UI. Copy YAML from the raw configuration editor back into that file when you want to version changes.

If the dashboard is missing after switching modes, redeploy once. If it still does not appear, delete the app volume and redeploy so the seed runs on a fresh Home Assistant instance.

## Deploy With Dokploy

Create a Dokploy Compose app from this repository and use `docker-compose.yml`.

Configure Dokploy to route traffic to:

- Service: `homeassistant`
- Container port: `8123`

The first time the app starts, open the routed URL and complete Home Assistant onboarding. Home Assistant stores auth and runtime state in the `homeassistant-config` Docker volume.

## Bundle Version

The demo vendors the built card bundle at:

```text
www/nvision/nvision.js
```

To update the public demo bundle, rebuild the card repo and copy its `dist/nvision.js` to this path before redeploying.

## Public Access

Home Assistant requires authentication for normal dashboard access. For a public demo, create a limited demo user after onboarding and share that flow however you prefer.

Do not commit Home Assistant runtime storage, passwords, tokens, `.env`, or pre-baked auth files.

## Demo Contents

The dashboard includes demo entities for:

- Activity
- Air quality
- Circle gauge
- Liquid
- Power draw
- Power glance
- Waveform
- Heat map
- Entity overview
- Reactor temperature
- Stat
- Sum
- Event log

The blank and light cards are intentionally excluded from this public demo.
