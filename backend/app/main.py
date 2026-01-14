from fastapi import FastAPI
from app.api.audit_api import router as audit_router
from app.api.health_api import router as health_router

app = FastAPI(title="SiteSage ApI", version="0.1.0")

app.include_router(health_router)
app.include_router(audit_router)


@app.get("/")
async def greetings():
    return "Welcome to SiteSage"

