from fastapi import FastAPI
from pydantic import BaseModel
import cognee
import asyncio

app = FastAPI()

class JobInput(BaseModel):
    company: str
    role: str
    notes: str

class QuestionInput(BaseModel):
    question: str

@app.post("/remember")
async def remember_job(job: JobInput):
    text = f"Company: {job.company}. Role: {job.role}. Notes: {job.notes}"
    await cognee.remember(text,dataset_name ="job_applications")
    return {"status":"saved","company":job.company}

@app.post("/recall")
async def recall_memory(q: QuestionInput):
    results = await cognee.recall(q.question, datasets =["job_applications"])
    answers = [r.text for r in results]
    return {"question": q.question, "answer": answers}