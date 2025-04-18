from rag import rag_response

# Interactive chatbot loop

def chatbot():
    print("Welcome to the RAG Chatbot! Type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break

        response = rag_response(user_input)
        print(f"Bot: {response}")
