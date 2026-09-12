from fastapi import FastAPI

app = FastAPI(
    title="RecoverAI",
    description="AI-powered revenue recovery system",
    version="0.1.0"
)


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