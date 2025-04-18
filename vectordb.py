import os 

import chromadb 
from chromadb.config import Settings

from embeddings import embedding_model
from llms import llm 

# define persistent directory
chroma_database_location = 'chromadb'
os.makedirs(chroma_database_location, exist_ok=True)


# Configure chromadb settings for persistent
chroma_settings = Settings(
    persist_directory = chroma_database_location,
    anonymized_telemetry = False
)

# Initialize ChromaDB client
client = chromadb.Client(chroma_settings)

# Create or get collection
collection_name = "chatbot_responses"

try:
    if collection_name in [c.name for c in client.list_collections()]:
        client.delete_collection(name=collection_name)
    collection = client.create_collection(name=collection_name)
except Exception as e:
    print(f"Error with collection : {e}")
    raise

# Sample dataset: question-response pairs
responses = [
    {"id": "1", "text": "Hello! How can I assist you today?", "trigger": "hi"},
    {"id": "2", "text": "AI is a field of computer science focused on building systems that can perform tasks like reasoning, learning, and decision-making.", "trigger": "what is ai"},
    {"id": "3", "text": "I can help with questions about AI, coding, or general knowledge. What's on your mind?", "trigger": "what can you do"},
    {"id": "4", "text": "Python is a versatile programming language great for AI, web development, and more.", "trigger": "tell me about python"},
    {"id": "5", "text": "Vector databases store embeddings for fast similarity searches, like in recommendation systems or chatbots.", "trigger": "what is a vector database"}
]

# Store data in Chromadb
triggers = [item['trigger'] for item in responses]
embeddings = embedding_model.encode(triggers).tolist()
ids = [item['id'] for item in responses]
metadatas = [{"text": item['text']} for item in responses]

collection.add(
    embeddings=embeddings,
    ids = ids,
    metadatas=metadatas
)
