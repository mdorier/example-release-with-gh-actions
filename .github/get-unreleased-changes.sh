#!/bin/bash

sed -n "/^\#\#\s\[Unreleased\]/,/^\#\#\s/p" CHANGELOG.md | grep -v "^##\s"
