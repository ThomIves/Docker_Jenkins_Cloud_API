from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "I think that it is working now :-) "}
