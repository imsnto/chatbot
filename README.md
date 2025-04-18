# RAG Chatbot

This project implements a **Retrieval-Augmented Generation (RAG)** chatbot that retrieves context from a ChromaDB vector database and generates responses using the Groq API (`llama-3.3-70b-versatile`) or a fallback `distilgpt2` model. The chatbot supports interactive command-line conversations and API-based querying via FastAPI, with embeddings generated by SentenceTransformer (`all-MiniLM-L6-v2`).

## Features
- **RAG Pipeline**: Combines retrieval from ChromaDB with response generation via Groq API or local LLM.
- **Persistent Vector Storage**: Stores question-response pairs in ChromaDB (`chromadb` directory).
- **FastAPI Server**: Exposes a `/query` endpoint for API-based interaction.
- **Interactive CLI**: Command-line interface for local testing (`chatbot.py`).
- **Modular Design**: Separates concerns into `app.py`, `chatbot.py`, `embedding.py`, `llms.py`, `rag.py`, and `vectordb.py`.
- **Exit Command**: Type `exit` in CLI to end the conversation.
- **Environment Variables**: Securely stores Groq API key in `.env`.

## Prerequisites
- **Python 3.8+**
- **Groq API Key**: Obtain from [console.groq.com](https://console.groq.com/keys).
- **Dependencies**: Listed in `requirements.txt` (e.g., `chromadb`, `sentence-transformers`, `fastapi`).

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/imsnto/chatbot.git
   cd chatbot
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install and Configure Ollama**:
   - Install Ollama: Follow instructions at [ollama.ai](https://ollama.ai/).
   - Pull the `qwen2.5:0.5b` model:
     ```bash
     ollama pull qwen2.5:0.5b
     ```
   - Ensure the Ollama server is running:
     ```bash
     ollama serve
     ```
5. **Configure HF and Groq API Key:**
   - Create a `.env` file in the project root:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   HF_TOKEN=your huggingface token
   ```
   - Ensure `.env` is listed in .gitignore.


## Usage
   **Interactive CLI**
1. Run the chatbot script:
   ```bash
   python main.py
   ```
   or
   ```bash
   python chatbot.py
   ```

2. Interact with the chatbot:
   - Enter your message at the `You: ` prompt.
   - Type `exit` to quit.
   - Example interaction:
     ```
     You: Hello, how are you?
     Bot: I'm doing great, thanks for asking! How about you?
     You: I'm learning LangChain.
     Bot: Nice! LangChain is awesome for building AI apps. Want tips?
     You: exit
     ```
**FastAPI Server**
1. Start the server:
   ```bash
   python app.py
   ```

## Project Structure
```
├── .env                    # Environment variables (GROQ_API_KEY)
├── .gitignore              # Ignores venv/, __pycache__/, .env
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── app.py                  # FastAPI server for API-based querying
├── chatbot.py              # Interactive CLI for local testing
├── embedding.py            # SentenceTransformer embedding model
├── llms.py                 # Groq API and distilgpt2 LLM setup
├── rag.py                  # RAG pipeline (retrieval + generation)
├── vectordb.py             # ChromaDB setup and sample data
└── chromadb/               # Persistent ChromaDB storage        
```

## Notes
- Ensure the Ollama server is running before executing `main.py`.
- The `.gitignore` file should include `.venv/` and other irrelevant files (e.g., `__pycache__/`, `.env`).
- The chatbot maintains conversation history in memory during the session. History is reset when the script exits.
- **Groq API:** Requires an active internet connection and valid API key. Rate limits apply (e.g., 30 requests/minute for free tier).
- **Fallback LLM:** Uses distilgpt2 locally if Groq API is unavailable (commented in llms.py).



## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

## License
This project is licensed under the MIT. See the [LICENSE](LICENSE) file for details.

## Resources
- [LangChain Documentation](https://python.langchain.com/docs/)
- [Ollama GitHub](https://github.com/ollama/ollama)
- [qwen2.5 Model](https://ollama.ai/library/qwen2.5)
