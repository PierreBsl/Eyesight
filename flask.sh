#!/bin/bash
export DB_USERNAME="admin"
export DB_PASSWORD="admin"
export FLASK_APP=run.py
export FLASK_ENV=dvp
flask run --host=0.0.0.0
