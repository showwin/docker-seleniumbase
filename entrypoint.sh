#!/bin/bash

python -m venv local/service
source "local/service/bin/activate"

seleniumbase install chromedriver

exec "$@"
