from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "The SUPER Hard Core Method!"}
