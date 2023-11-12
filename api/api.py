from fastapi import FastAPI

app = FastAPI()

@app.get("new/api")
async def api():
    return {"true" : "NEw API Hits"}