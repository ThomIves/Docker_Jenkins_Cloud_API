from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Thom Ives and World! You too can serve REST APIs!"}
