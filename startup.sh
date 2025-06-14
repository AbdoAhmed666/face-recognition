#!/bin/bash

# Activate the virtual environment if exists (optional)
# source /home/site/wwwroot/venv/bin/activate

# Run with python -m streamlit to avoid PATH issues
python -m streamlit run web/application.py --server.port $PORT --server.enableCORS false
