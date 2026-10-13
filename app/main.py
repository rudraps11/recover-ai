from fastapi import FastAPI
from app.routers import payments


app = FastAPI(
    title="RecoverAI",
    description="AI-powered revenue recovery system",
    version="0.1.0"
)


app.include_router(payments.router)


@app.get("/")
def root():
    return {
        "message": "RecoverAI is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }