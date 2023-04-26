# project/app/main.py


from fastapi import FastAPI, Depends

from app.config import get_settings, Settings

app = FastAPI(title="Testdriven.io FastAPI and Docker")


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }