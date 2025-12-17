# Quick Start - LocalGPT Vision

## Get Running in 3 Minutes

### 1. Install Dependencies (1 minute)

```bash
pip install -r requirements.txt
```

### 2. Setup API Keys (1 minute)

```bash
# Copy the environment template
cp .env.example .env

# Edit with your favorite editor
nano .env
```

Add your API keys (get them from these links):
- **Google Gemini** (FREE): https://aistudio.google.com/app/apikey
- **Groq** (FREE): https://console.groq.com/keys
- **OpenAI** (Paid): https://platform.openai.com/api-keys

Example `.env` file:
```
GOOGLE_API_KEY=AIzaSyC_your_actual_key_here
GROQ_API_KEY=gsk_your_actual_key_here
OPENAI_API_KEY=sk-your_actual_key_here
```

### 3. Start Application (30 seconds)

```bash
# Test your APIs (optional)
python test_all_apis.py

# Start the app
python app.py
```

**Open in browser:** http://localhost:5050

## Or Use The Automated Script

```bash
# One command to set up and run everything
./start.sh
```

## First Steps After Starting

1. **Create a session**: Click "New Session" in sidebar
2. **Upload documents**: Click the paperclip icon, select PDFs/images
3. **Index files**: Click "Start Indexing" and wait
4. **Ask questions**: Type your question and press Enter
5. **View results**: See retrieved pages and AI-generated answer

## Choose Your Model

Click **Models** button (top right) to select:

### Best for Free Users
- **Retrieval**: vidore/colpali
- **Generation**: Google Gemini or Groq Llama Vision

### Best for Quality (Paid)
- **Retrieval**: vidore/colqwen2-v0.1
- **Generation**: OpenAI GPT-4

### Best for Privacy (100% Local)
- **Retrieval**: vidore/colpali
- **Generation**: Qwen2-VL-7B or Molmo

## What You Can Do

- Upload PDFs, Word docs, or images
- Ask questions about your documents
- Get answers with relevant page citations
- Chat with multiple document sources
- Switch between different AI models
- Manage multiple chat sessions
- Export conversations

## Common Questions

**Q: Which API key do I need?**
A: At minimum, get Google Gemini (it's free). Add others as needed.

**Q: Can I use it without any API keys?**
A: Yes! Use local models like Qwen or Molmo. They download automatically but need 16GB+ RAM.

**Q: How much does it cost?**
A: Google Gemini and Groq have free tiers. OpenAI is paid (~$0.01-0.05 per query).

**Q: Is my data private?**
A: Cloud models (Gemini, GPT-4) send data to their APIs. Local models keep everything on your machine.

**Q: What file types are supported?**
A: PDF, DOC, DOCX, PNG, JPG, JPEG

## Troubleshooting

**App won't start?**
```bash
# Check Python version (need 3.8+)
python --version

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

**"API Key not found" error?**
- Make sure `.env` file exists in project root
- Check there are no extra spaces in the keys
- Restart the app after editing `.env`

**Out of memory?**
- Use cloud models (Gemini/Groq) instead of local
- Reduce image size in Settings
- Close other applications

## What's Next?

- Read [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions
- Check [API_INTEGRATION_GUIDE.md](API_INTEGRATION_GUIDE.md) for API setup
- See [README.md](README.md) for architecture details

## Support

Need help? Check:
1. `app.log` file for error details
2. Console output when running app
3. Test your APIs: `python test_all_apis.py`

Enjoy using LocalGPT Vision!
