
from src.utils.embeddings import embedding_model
from src.utils.llms import llm, call_groq
from src.services.vectordb import collection

# RAG function: Retrieve context and generate response with LLM
def rag_response(query: str, top_k: int = 2, min_similarity: float = 0.3) -> str:
    try:
        #  convert query to embedding
        query_embedding = embedding_model.encode(query).tolist()

        # Query ChromaDB
        results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
        
        contexts = []
        # Filter by similarity
        for distance, metadata in zip(results['distances'][0], results['metadatas'][0]):
            similarity = 1 - distance 
            if similarity >= min_similarity:
                contexts.append(metadata['text'])

        if not contexts:
            return "Sorry, I don't have enough information. Can you rephrase?"
        
        # Create prompt for LLM
        context = "\n".join(contexts)
        prompt = f"Context:\n{context}\n\nQuery: {query}\nAnswer concisely:"

        # Generate response
        # response = llm(prompt)[0]['generated_text']
        # answer = response.split("Anser concisely:")[-1].strip()

        answer = call_groq(prompt)
        return answer
    
    except Exception as e:
        print(e)
    return ""
