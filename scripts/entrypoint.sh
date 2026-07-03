#!/bin/sh
set -e

python3 /bootstrap/seed-dashboard.py
exec /init
