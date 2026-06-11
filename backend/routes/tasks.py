from fastapi import APIRouter
from database.db import SessionLocal
from database.models import Task
from schemas.task_schema import TaskCreate

router = APIRouter()

@router.post("/task")
def create_task(task: TaskCreate):

    db = SessionLocal()

    new_task = Task(
        title=task.title
    )

    db.add(new_task)
    db.commit()

    return {
        "message": "Task Created"
    }


@router.get("/tasks")
def get_tasks():

    db = SessionLocal()

    return db.query(Task).all()


@router.put("/task/{task_id}")
def complete_task(task_id: int):

    db = SessionLocal()

    task = (
        db.query(Task)
        .filter(Task.id == task_id)
        .first()
    )

    if not task:
        return {
            "error": "Task not found"
        }

    task.status = "completed"

    db.commit()

    return {
        "message": "Task completed",
        "task_id": task_id
    }

@router.delete("/task/{task_id}")
def delete_task(task_id: int):

    db = SessionLocal()

    task = (
        db.query(Task)
        .filter(Task.id == task_id)
        .first()
    )

    if not task:
        return {
            "error": "Task not found"
        }

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted",
        "task_id": task_id
    }