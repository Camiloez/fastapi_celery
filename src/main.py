from fastapi import FastAPI, Request
import time
from task import create_task


app = FastAPI()


@app.get("/")
async def home(request: Request):
    return {
        "message": "hello"
    }

@app.get("/task")
async def task(request: Request):
    id = create_task.delay(5)

    return {
        "message": f"Generated a task to celery, {id}"
    }