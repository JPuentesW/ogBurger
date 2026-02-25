from fastapi import FastAPI
import os

app = FastAPI(title="OG Burger API")

@app.get("/")
def root():
    return {"message": "OG Burger API OK"}

@app.get("/health")
def health():
    return {
        "status": "ok",
        "app_env": os.getenv("APP_ENV"),
        "db_host": os.getenv("DB_HOST"),
        "db_name": os.getenv("DB_NAME"),
    }