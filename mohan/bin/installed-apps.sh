#!/usr/bin/env bash

# https://github.com/omacom/omarchy/install/omarchy-base.packages

grep -vFx -f apps-preinstalled.txt apps.txt > installed-apps.txt
expac --timefmt='%Y-%m-%d %T' '%l\t%w\t%n'|grep explicit |cut -f1,3|sort > explicit-apps.txt
