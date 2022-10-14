from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hey - Did it work?"}
