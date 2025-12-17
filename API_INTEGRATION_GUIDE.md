# API Integration Guide

## Complete API Setup for All Models

This guide shows you exactly how to integrate each API into the LocalGPT Vision application.

## 1. Google Gemini API Integration

### Get API Key
1. Go to https://aistudio.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy the key (starts with `AIza...`)

### Add to .env
```bash
GOOGLE_API_KEY=AIzaSyC_your_actual_key_here
```

### Test Integration
```python
# Test script: test_gemini.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash-002')

response = model.generate_content("Hello, are you working?")
print(response.text)
```

### Usage in Application
- Select "Google Gemini" in Settings
- Supports multiple images
- Fast and free (with limits)

## 2. OpenAI GPT-4 Vision API Integration

### Get API Key
1. Go to https://platform.openai.com/api-keys
2. Sign in or create account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-...`)
5. Add payment method (GPT-4 is paid only)

### Add to .env
```bash
OPENAI_API_KEY=sk-your_actual_key_here
```

### Test Integration
```python
# Test script: test_openai.py
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Hello, are you working?"}
    ]
)

print(response.choices[0].message.content)
```

### Usage in Application
- Select "OpenAI GPT-4" in Settings
- Best quality responses
- Supports multiple images
- Paid per token

### Pricing
- GPT-4o: $2.50/1M input tokens, $10/1M output tokens
- GPT-4o-mini: $0.15/1M input tokens, $0.60/1M output tokens

## 3. Groq API Integration

### Get API Key
1. Go to https://console.groq.com/keys
2. Sign up for free account
3. Click "Create API Key"
4. Copy the key (starts with `gsk_...`)

### Add to .env
```bash
GROQ_API_KEY=gsk_your_actual_key_here
```

### Test Integration
```python
# Test script: test_groq.py
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.2-90b-text-preview",
    messages=[
        {"role": "user", "content": "Hello, are you working?"}
    ]
)

print(response.choices[0].message.content)
```

### Usage in Application
- Select "Groq Llama Vision" in Settings
- Very fast inference
- Free tier available
- Single image only

### Rate Limits (Free Tier)
- 30 requests per minute
- 14,400 requests per day

## 4. Local Models (No API Keys)

### Qwen2-VL-7B-Instruct

**Requirements:**
- 16GB RAM minimum
- Apple Silicon or NVIDIA GPU

**Setup:**
```bash
# Models download automatically on first use
# Stored in: ~/.cache/huggingface/
```

**Usage:**
- Select "Qwen2-VL-7B-Instruct" in Settings
- Fully local, no internet needed after download
- Good quality, moderate speed

### Llama-Vision

**Requirements:**
- 16GB RAM minimum
- CUDA GPU or Apple Silicon

**Setup:**
```bash
# Automatically downloads from HuggingFace
```

**Usage:**
- Select "Llama-Vision" in Settings
- Single image processing
- Good for simple queries

### Pixtral-12B

**Requirements:**
- 16GB RAM minimum
- Downloads ~12GB model

**Setup:**
```bash
# Model downloads to: ./mistral_models/Pixtral/
```

**Usage:**
- Select "Pixtral" in Settings
- Mistral's vision model
- Single image only

### Molmo

**Requirements:**
- 8GB RAM minimum
- Smallest local model

**Setup:**
```bash
# Downloads automatically from HuggingFace
# Model: allenai/MolmoE-1B-0924
```

**Usage:**
- Select "Molmo" in Settings
- Fast and efficient
- Good for lower-end hardware

### Ollama Llama Vision

**Requirements:**
- Ollama installed locally

**Setup:**
```bash
# Install Ollama
# macOS/Linux:
curl -fsSL https://ollama.ai/install.sh | sh

# Or download from: https://ollama.ai

# Pull the model
ollama pull llama3.2-vision

# Start Ollama service
ollama serve
```

**Usage:**
- Select "Ollama Llama Vision" in Settings
- Uses local Ollama service
- Single image processing

## 5. Complete .env File Example

```bash
# Google Gemini (Free tier available)
GOOGLE_API_KEY=AIzaSyC1234567890abcdefghijklmnop

# OpenAI (Paid)
OPENAI_API_KEY=sk-1234567890abcdefghijklmnopqrstuvwxyz

# Groq (Free tier available)
GROQ_API_KEY=gsk_1234567890abcdefghijklmnopqrstuvwxyz

# Flask
SECRET_KEY=change-this-to-a-random-secret-key
FLASK_ENV=development
```

## 6. Verification Script

Create `test_all_apis.py`:

```python
import os
from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI
from groq import Groq

load_dotenv()

print("Testing API Connections...\n")

# Test Google Gemini
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash-002')
        response = model.generate_content("Say 'OK'")
        print("✓ Google Gemini API: Working")
    else:
        print("✗ Google Gemini API: Key not found")
except Exception as e:
    print(f"✗ Google Gemini API: Error - {e}")

# Test OpenAI
try:
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": "Say 'OK'"}],
            max_tokens=5
        )
        print("✓ OpenAI API: Working")
    else:
        print("✗ OpenAI API: Key not found")
except Exception as e:
    print(f"✗ OpenAI API: Error - {e}")

# Test Groq
try:
    api_key = os.getenv("GROQ_API_KEY")
    if api_key:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.2-90b-text-preview",
            messages=[{"role": "user", "content": "Say 'OK'"}],
            max_tokens=5
        )
        print("✓ Groq API: Working")
    else:
        print("✗ Groq API: Key not found")
except Exception as e:
    print(f"✗ Groq API: Error - {e}")

print("\nAPI verification complete!")
```

Run it:
```bash
python test_all_apis.py
```

## 7. Cost Estimation

### Free Options
- **Google Gemini**: 60 requests/min, 1500/day (free)
- **Groq**: 30 requests/min, 14,400/day (free)
- **Local Models**: Unlimited, free (one-time download)

### Paid Options
- **OpenAI GPT-4o**: ~$0.01-0.05 per query (with images)

### Example: 100 Document Queries
- **Gemini**: Free
- **Groq**: Free
- **GPT-4**: ~$1-5
- **Local**: Free

## 8. Best Practices

### API Key Security
```bash
# Never commit .env to git
echo ".env" >> .gitignore

# Use environment variables in production
export GOOGLE_API_KEY="your-key"

# Rotate keys regularly
# Set up key rotation every 90 days
```

### Error Handling
```python
try:
    response = model.generate_content(prompt)
except Exception as e:
    if "quota" in str(e).lower():
        print("API quota exceeded. Try another model.")
    elif "authentication" in str(e).lower():
        print("Invalid API key. Check .env file.")
    else:
        print(f"Error: {e}")
```

### Rate Limiting
```python
import time

def rate_limited_api_call(func, *args, **kwargs):
    max_retries = 3
    for i in range(max_retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if "rate limit" in str(e).lower():
                wait_time = (2 ** i) * 5  # Exponential backoff
                print(f"Rate limited. Waiting {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise
    raise Exception("Max retries exceeded")
```

## 9. Troubleshooting

### "Invalid API Key"
- Check `.env` file exists in project root
- Verify key is copied correctly (no extra spaces)
- Restart Flask application after adding keys

### "Quota Exceeded"
- Wait for quota reset (usually 24 hours)
- Switch to different model
- Use local models as fallback

### "Connection Error"
- Check internet connection
- Verify API service is up (check status pages)
- Try different model

### Model Not Loading
- Check disk space (models are 1-12GB)
- Verify internet connection for download
- Check `~/.cache/huggingface/` for downloads

## 10. Quick Start Commands

```bash
# Complete setup in one go
cp .env.example .env
# Edit .env with your API keys
pip install -r requirements.txt
python test_all_apis.py
python app.py
```

Access at: http://localhost:5050

Done! All APIs are now integrated and ready to use.
