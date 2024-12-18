#!/bin/bash

# Load environment variables from .env file
source .env
# Activate the virtual environment
source "$VENV/bin/activate"
# Run the FastAPI app
uvicorn nerc_api.main:app --host "$HOST" --port "$PORT"
