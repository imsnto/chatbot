from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
    Answer the following questions:

    Here is the the conversation history: {context}

    Question: {question}

    Answer:
"""

#deepseek-r1:1.5b
#qwen2.5:0.5b

model = OllamaLLM(model="qwen2.5:0.5b")

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        result = chain.invoke({"context": context, "question": user_input})
        print("Bot: ", result)

        context += f"\nUser: {user_input}\nAI: {result}"


if __name__ == "__main__":
    handle_conversation()