from fastapi import FastAPI
from backend.agents import start_task
from backend.database import init_db

app = FastAPI(title="Multi-Agent Automation MVP")

@app.on_event("startup")
def startup_event():
    init_db()

@app.post("/task/{task_name}")
async def create_task(task_name: str):
    result = await start_task(task_name)
    return {"status": "started", "task": task_name, "result": result}

@app.get("/health")
def health_check():
    return {"status": "ok"}
