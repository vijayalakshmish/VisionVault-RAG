#!/bin/bash

echo "=========================================="
echo "LocalGPT Vision - Starting Application"
echo "=========================================="
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo ""
    echo "Please edit .env file and add your API keys:"
    echo "  - GOOGLE_API_KEY (for Gemini)"
    echo "  - OPENAI_API_KEY (for GPT-4)"
    echo "  - GROQ_API_KEY (for Groq)"
    echo ""
    echo "Then run this script again."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "Installing/updating dependencies..."
pip install -q -r requirements.txt

# Test APIs
echo ""
echo "Testing API connections..."
python test_all_apis.py

# Start the application
echo ""
echo "Starting Flask application..."
echo "Access the application at: http://localhost:5050"
echo ""
python app.py
