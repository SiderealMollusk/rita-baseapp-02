import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def read_hello():
    version = os.getenv("APP_VERSION", "unknown")
    return {"message": f"Hello from version {version}"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
