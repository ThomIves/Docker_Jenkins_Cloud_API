from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is a small change to our VERY simple API."}
