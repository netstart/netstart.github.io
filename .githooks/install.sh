#!/bin/sh
# Aponta os hooks deste repositório para a pasta versionada .githooks.
cd "$(dirname "$0")/.." || exit 1
git config core.hooksPath .githooks && echo "Hooks instalados: core.hooksPath = .githooks"
