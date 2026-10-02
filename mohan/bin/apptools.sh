#!/usr/bin/env bash

# List explicitly-installed packages that are neither omarchy baseline nor infra.
# Subtracts the baseline and the infrastructure blocklist (kernel, firmware,
# audio stack, DE packages) to isolate real apps/tools.

# https://github.com/omacom/omarchy/install/omarchy-base.packages

# usage: apptools.sh [explicit-file] [baseline-file] [infra-file]

explicit=${1:-explicit-apps.txt}
baseline=${2:-apps-preinstalled.txt}
infra=${3:-apps-infrastructure.txt}

cut -f2 "$explicit" | grep -vFx -f "$baseline" -f "$infra" | sort -u
