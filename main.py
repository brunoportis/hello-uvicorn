from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hello"}

@app.get("/world")
async def world():
    return {"message": "World"}
