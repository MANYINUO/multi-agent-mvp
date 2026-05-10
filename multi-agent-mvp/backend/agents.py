import asyncio
from .tasks import run_task
from .notifiers import notify

async def start_task(task_name: str):
    results = await asyncio.gather(
        run_task(task_name + "_agent1"),
        run_task(task_name + "_agent2"),
    )
    await notify(f"Task {task_name} completed with results: {results}")
    return results
