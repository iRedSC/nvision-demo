# nvision demo

Standalone Home Assistant demo for the nvision dashboard cards.

This repo is intentionally separate from [`iRedSC/nvision`](https://github.com/iRedSC/nvision). It owns only the public demo deployment: Docker Compose, Home Assistant demo configuration, and Lovelace dashboard YAML.

## Run Locally

```bash
cp .env.example .env
docker compose up -d
```

Open `http://localhost:8123`, complete Home Assistant onboarding, then open the preloaded **nvision Demo** dashboard.

The demo loads the card bundle from `/local/nvision/nvision.js`. On startup, the `nvision-bundle` service downloads that file into a Docker volume from `NVISION_BUNDLE_URL`.

## Deploy With Dokploy

Create a Dokploy Compose app from this repository and use `compose.yml`.

Configure Dokploy to route traffic to:

- Service: `homeassistant`
- Container port: `8123`

The first time the app starts, open the routed URL and complete Home Assistant onboarding. Home Assistant stores auth and runtime state in the `homeassistant-config` Docker volume.

## Bundle Version

By default, the demo tracks the committed bundle on `main`:

```env
NVISION_BUNDLE_URL=https://raw.githubusercontent.com/iRedSC/nvision/main/dist/nvision.js
```

For a stable public demo, set `NVISION_BUNDLE_URL` in Dokploy to a pinned release or tag URL after publishing one.

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
