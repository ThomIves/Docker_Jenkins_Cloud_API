from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "With the script generator ..."}
