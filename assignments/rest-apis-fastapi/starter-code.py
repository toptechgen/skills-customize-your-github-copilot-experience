from fastapi import FastAPI, HTTPException

app = FastAPI()

# Starter tasks stored in memory
TASKS = [
    {"id": 1, "title": "Learn FastAPI"},
    {"id": 2, "title": "Build a REST API"},
]


@app.get("/")
def read_root():
    # TODO: Return the API name and status as a dictionary.
    pass


@app.get("/tasks")
def get_tasks():
    # TODO: Return all tasks.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Find and return the task with the matching ID.
    # If no task is found, raise HTTPException(status_code=404).
    pass


@app.post("/tasks")
def create_task(title: str):
    # TODO: Create a new task with the next available ID.
    # Return the newly created task.
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Remove the matching task and return it.
    # If no task is found, raise HTTPException(status_code=404).
    pass
