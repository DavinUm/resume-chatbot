"""
AI Resume Chatbot - FastAPI Entry Point
RAG-powered backend for the interactive portfolio chatbot.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Resume Chatbot API",
    description="RAG-powered backend for answering questions about professional experience",
    version="0.1.0",
)

# CORS middleware for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict to your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    """Verify the server is running."""
    return {"status": "ok", "message": "AI Resume Chatbot API is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
