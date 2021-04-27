#!/bin/bash

set -euo pipefail

cd $(dirname $0)
source config
wait
python scripts/crack-zip.py -i ${filename}.zip
