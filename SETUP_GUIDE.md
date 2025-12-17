# Complete Setup Guide - LocalGPT Vision

## Quick Start (5 Minutes)

### Step 1: Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt
```

### Step 2: Configure API Keys

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API keys
nano .env  # or use any text editor
```

**Get Your API Keys:**

1. **Google Gemini API** (Free tier available)
   - Visit: https://aistudio.google.com/app/apikey
   - Click "Create API Key"
   - Copy and paste into `.env` file

2. **OpenAI API** (Paid)
   - Visit: https://platform.openai.com/api-keys
   - Create new secret key
   - Copy and paste into `.env` file

3. **Groq API** (Free tier available)
   - Visit: https://console.groq.com/keys
   - Create API key
   - Copy and paste into `.env` file

### Step 3: Run the Application

```bash
# Start the Flask server
python app.py
```

The application will start at: **http://localhost:5050**

## Available Models

### Cloud Models (Require API Keys)
- **Google Gemini** - Fast, free tier available, excellent for documents
- **OpenAI GPT-4** - Best quality, paid only
- **Groq Llama Vision** - Fast inference, free tier available

### Local Models (No API Keys Needed)
- **Qwen2-VL-7B** - Good balance of speed and quality
- **Llama-Vision** - Meta's vision model
- **Pixtral** - Mistral's vision model
- **Molmo** - Allen AI's efficient model
- **Ollama Llama Vision** - Requires Ollama installed locally

## Usage Instructions

### 1. Start a New Session
- Click "New Session" button in sidebar
- A new chat session will be created

### 2. Upload and Index Documents
- Click the paperclip icon (📎) to upload files
- Supported formats: PDF, DOC, DOCX, Images
- Click "Start Indexing" when prompted
- Wait for indexing to complete

### 3. Ask Questions
- Type your question in the chat input
- The system will:
  - Retrieve relevant document pages
  - Show the retrieved images
  - Generate an answer using the selected model

### 4. Change Models
- Click "Models" button in top right
- Select your preferred retrieval and generation models
- Save settings

## Model Recommendations

### For Best Quality
- **Retrieval Model:** vidore/colqwen2-v0.1
- **Generation Model:** OpenAI GPT-4 or Google Gemini

### For Speed
- **Retrieval Model:** vidore/colpali
- **Generation Model:** Groq Llama Vision or Molmo

### For Privacy (100% Local)
- **Retrieval Model:** vidore/colpali
- **Generation Model:** Qwen2-VL-7B or Llama-Vision

## Troubleshooting

### Issue: "API Key not found"
**Solution:** Make sure you created `.env` file and added your API keys

### Issue: "Module not found"
**Solution:** Run `pip install -r requirements.txt`

### Issue: Out of memory with local models
**Solution:**
- Use smaller models (Molmo, Groq)
- Reduce image dimensions in Settings
- Close other applications

### Issue: Slow indexing
**Solution:**
- Normal for first run (downloads models)
- Use vidore/colpali for faster indexing
- Reduce image dimensions

### Issue: Ollama model not working
**Solution:**
- Install Ollama: https://ollama.ai
- Run: `ollama pull llama3.2-vision`
- Start Ollama service

## API Rate Limits

### Google Gemini (Free Tier)
- 60 requests per minute
- 1500 requests per day

### Groq (Free Tier)
- 30 requests per minute
- 14,400 requests per day

### OpenAI (Paid)
- Varies by tier
- Check: https://platform.openai.com/account/rate-limits

## Advanced Configuration

### Adjust Image Quality
Settings → Image Settings
- Higher values = Better quality, slower processing
- Lower values = Faster, lower quality
- Default: 280x280 (good balance)

### Change Retrieval Count
Edit `models/retriever.py`:
```python
results = RAG.search(query, k=5)  # Retrieve 5 documents instead of 3
```

### Enable Debug Mode
Edit `.env`:
```
FLASK_DEBUG=True
```

## System Requirements

### Minimum (Cloud Models Only)
- 4GB RAM
- Any CPU
- Internet connection

### Recommended (Local Models)
- 16GB RAM
- Apple Silicon M1/M2/M3 or NVIDIA GPU
- 20GB free disk space

## Security Notes

- Keep `.env` file private (never commit to git)
- Use environment variables for API keys
- Rotate API keys regularly
- Monitor API usage on provider dashboards

## Support

For issues or questions:
- GitHub Issues: [Your repo URL]
- Check `app.log` for detailed error messages
- Review Flask console output

## Next Steps

1. Upload your first document
2. Try different models to see which works best
3. Adjust image settings for optimal performance
4. Explore chat sessions for different projects
