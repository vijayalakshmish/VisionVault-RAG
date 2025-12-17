import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 60)
print("API Connection Test for LocalGPT Vision")
print("=" * 60)
print()

# Test Google Gemini
print("1. Testing Google Gemini API...")
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key and api_key != "your_google_api_key_here":
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash-002')
        response = model.generate_content("Say 'OK'")
        print("   Status: Working")
        print(f"   Response: {response.text[:50]}")
    else:
        print("   Status: API Key not configured")
        print("   Action: Add GOOGLE_API_KEY to .env file")
except Exception as e:
    print(f"   Status: Error - {str(e)[:80]}")

print()

# Test OpenAI
print("2. Testing OpenAI GPT-4 API...")
try:
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key and api_key != "your_openai_api_key_here":
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": "Say 'OK'"}],
            max_tokens=5
        )
        print("   Status: Working")
        print(f"   Response: {response.choices[0].message.content}")
    else:
        print("   Status: API Key not configured")
        print("   Action: Add OPENAI_API_KEY to .env file")
except Exception as e:
    print(f"   Status: Error - {str(e)[:80]}")

print()

# Test Groq
print("3. Testing Groq API...")
try:
    api_key = os.getenv("GROQ_API_KEY")
    if api_key and api_key != "your_groq_api_key_here":
        from groq import Groq
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.2-90b-text-preview",
            messages=[{"role": "user", "content": "Say 'OK'"}],
            max_tokens=5
        )
        print("   Status: Working")
        print(f"   Response: {response.choices[0].message.content}")
    else:
        print("   Status: API Key not configured")
        print("   Action: Add GROQ_API_KEY to .env file")
except Exception as e:
    print(f"   Status: Error - {str(e)[:80]}")

print()

# Check local models
print("4. Checking Local Model Support...")
try:
    import torch
    print("   PyTorch: Installed")
    if torch.cuda.is_available():
        print("   CUDA: Available")
    elif torch.backends.mps.is_available():
        print("   MPS (Apple Silicon): Available")
    else:
        print("   Note: No GPU detected, using CPU")
except Exception as e:
    print(f"   PyTorch: Error - {str(e)[:80]}")

print()

# Check Ollama
print("5. Checking Ollama Installation...")
try:
    import subprocess
    result = subprocess.run(['ollama', '--version'],
                          capture_output=True,
                          text=True,
                          timeout=5)
    if result.returncode == 0:
        print("   Status: Installed")
        print(f"   Version: {result.stdout.strip()}")
    else:
        print("   Status: Not installed")
        print("   Action: Install from https://ollama.ai")
except FileNotFoundError:
    print("   Status: Not installed")
    print("   Action: Install from https://ollama.ai")
except Exception as e:
    print(f"   Status: Error - {str(e)[:80]}")

print()
print("=" * 60)
print("Test Complete!")
print("=" * 60)
print()
print("Next Steps:")
print("1. Configure missing API keys in .env file")
print("2. Run: python app.py")
print("3. Open: http://localhost:5050")
print()
