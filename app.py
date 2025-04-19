import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from rag import rag_response

app = FastAPI(
    title="RAG Chatbot",
    description="Chatting with you and retrieve context data from database",
    version="0.1.0"
)

class QueryRequest(BaseModel):
    query: str 


@app.post("/query")
async def query_chatbot(request: QueryRequest):
    try:
        response = rag_response(request.query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def get_frontend():
    return {
        "message": "Welcome to the RAG Chatbot API. Use POST /query to interact.",
        "example": {"query": "What is AI?"}
    }

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)