#!/bin/bash

folders=("frontend", "backend") 

for folder in "${folders[@]}"; do
  echo "Generating license file for $folder..."
  cd ../$folder && \
  license-checker --json > licenses.json && \
  cd .. && \
  python3 scripts/license_parser.py < $folder/licenses.json > $folder/license.html
  echo "License file generated for $folder."
done
