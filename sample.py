from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Job Memory Agent running"}