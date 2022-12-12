#!/usr/bin/env bash

set -euo pipefail

BASEDIR=$(dirname $PWD/..)

echo "=== Started Initializing Insurance Service ==="

echo "==> Creating Virtualenv"
cd $BASEDIR
python3 -m venv ./venv
source venv/bin/activate

echo "==> Insalling dev dependencies"
cd $BASEDIR
pip install -r requirements.txt
