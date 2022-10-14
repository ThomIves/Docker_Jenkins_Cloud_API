from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hey - Need to Watch For Changes On Remote, So I Am Studying That."}
