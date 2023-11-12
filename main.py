from fastapi import FastAPI
from api import api
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/api")
async def api():
    return {"true" : "API Hits"}

app.include_router(api_v1_router, prefix="/api")
