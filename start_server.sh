#!/usr/bin/env bash

set -e # cause the script to exit on any errors

echo '[start_server.sh] Activating Virtual Environment'
source env/bin/activate
echo '[start_server.sh] Starting The Server'
python app.py