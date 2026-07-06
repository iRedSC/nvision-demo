# nvision demo

Standalone Home Assistant demo for the nvision dashboard cards.

This repo is intentionally separate from [`iRedSC/nvision`](https://github.com/iRedSC/nvision). It owns only the public demo deployment: Docker Compose, Home Assistant demo configuration, and Lovelace dashboard YAML.

## Run Locally

```bash
cp .env.example .env
docker compose up -d
```

Open `http://localhost:8123`, complete Home Assistant onboarding, then open **nvision Demo** in the sidebar.

The demo loads the checked-in card bundle from `/local/nvision/nvision.js`. On first boot, the container seeds a **storage-mode** dashboard from `demo/home-assistant/ui-lovelace.yaml`, so you can edit it with the normal Lovelace UI.

Add demo controls anywhere with the reusable card in [`demo/lovelace/demo-controls-card.yaml`](demo/lovelace/demo-controls-card.yaml). In the dashboard editor: **Add card → Manual**, then paste the YAML.

## Auto-login

Trusted-network auto-login is unreliable behind reverse proxies, so the demo uses a landing page instead.

1. Set `DEMO_USERNAME` and `DEMO_PASSWORD` in Dokploy to match your demo Home Assistant user.
2. Redeploy.
3. Route your public URL to **`/local/demo/`**, or send visitors there directly.

That page signs in through Home Assistant's login API and redirects to the demo dashboard. If auto-login fails, it shows the demo credentials and a link to the normal `/auth/login` page.

Patching or autofilling the built-in `/auth` page itself is not supported by Home Assistant.

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

- Activity (manual control)
- Air particulates (manual control)
- Tank level (manual control)
- Living room noise (simulated)
- Dining room noise (manual control)
- Outside temperature (simulated)
- Reactor temperature (manual control)
- PC power draw (manual control)
- Fridge, washer, dryer, dishwasher, and oven power draw (simulated)
- Appliance running costs tied to power draw (simulated)
- Battery level (manual control)
- Wind speed (manual control)
- Door switch (simulated every 5–30 seconds)
- Laundry cycle timer (2-minute auto loop)
- Circle gauge, liquid, waveform, heat map, entity overview, stat, sum, and event log cards

The blank and light cards are intentionally excluded from this public demo.
