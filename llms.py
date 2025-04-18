from transformers import pipeline 
import requests
from dotenv import load_dotenv
import os 
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize  LLM
llm = pipeline('text-generation', model='distilgpt2', max_new_tokens=100)

# Groq API client 
def call_groq(prompt, model="llama-3.3-70b-versatile"):
    
    # client = Groq(
    #     api_key=GROQ_API_KEY
    # )
    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant providing concise and accurate answers."},
    #         {"role": "user", "content": prompt}
    #     ],
    #     model="llama-3.3-70b-versatile",
    # )
    # response = chat_completion.choices[0].message.content
    # return response

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant providing concise and accurate answers."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }
    
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']
    
