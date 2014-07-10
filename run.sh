#!/bin/bash

export SETTINGS='config.Config'

if [[ $1 == "dev" ]]; then
    python run_dev.py
else
    foreman start -p 8888
fi
