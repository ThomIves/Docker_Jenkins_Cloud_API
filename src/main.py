from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hey - Being More specific with ops on local machine using repo."}
