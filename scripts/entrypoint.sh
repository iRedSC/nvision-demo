#!/bin/sh
set -e

python3 /bootstrap/seed-dashboard.py
python3 /bootstrap/generate-demo-auth.py
exec /init
