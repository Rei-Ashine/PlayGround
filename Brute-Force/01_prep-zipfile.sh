#!/bin/bash

set -euo pipefail

source config
echo "This is target file." >> ${filename}.txt 
zip -e --password=${password} ${filename}.zip ${filename}.txt && rm ${filename}.txt
