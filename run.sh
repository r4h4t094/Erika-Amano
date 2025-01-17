#!/bin/bash

# Run Gunicorn for the app in the background
gunicorn app:app &

# Run the bot script
python3 -m Bot
