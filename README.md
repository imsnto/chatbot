# LangChain Ollama Chatbot

This project implements a conversational AI chatbot using LangChain and the Ollama `qwen2.5:0.5b` model. The chatbot maintains conversation history and responds to user inputs in an interactive command-line interface.

## Features
- **Conversational AI**: Uses LangChain to manage prompts and conversation context.
- **Ollama Integration**: Leverages the lightweight `qwen2.5:0.5b` model for fast responses.
- **Persistent Context**: Stores conversation history to provide context-aware replies.
- **Interactive CLI**: Simple command-line interface for user interaction.
- **Exit Command**: Type `exit` to end the conversation.

## Prerequisites
- Python 3.8+
- Ollama installed locally (with the `qwen2.5:0.5b` model pulled)
- Required Python packages: `langchain-ollama`, `langchain-core`

## Installation
1. **Clone the Repository**:
   ```bash
   git clone [<repository-url>](https://github.com/imsnto/chatbot.git)
   cd chatbot
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install langchain-ollama langchain-core
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

## Usage
1. Run the chatbot script:
   ```bash
   python main.py
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

## Project Structure
```
├── .gitignore             
├── LICENSE
├── main.py             
└── README.md             
```

## Notes
- Ensure the Ollama server is running before executing `main.py`.
- The `.gitignore` file should include `.venv/` and other irrelevant files (e.g., `__pycache__/`, `.env`).
- The chatbot maintains conversation history in memory during the session. History is reset when the script exits.

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
This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.

## Resources
- [LangChain Documentation](https://python.langchain.com/docs/)
- [Ollama GitHub](https://github.com/ollama/ollama)
- [qwen2.5 Model](https://ollama.ai/library/qwen2.5)
