from fastapi import APIRouter

from database.db import SessionLocal
from database.models import Task
from database.models import UserMemory
from database.models import Reminder

router = APIRouter()


@router.get("/daily-plan")
def daily_plan():

    db = SessionLocal()

    tasks = (
        db.query(Task)
        .filter(Task.status == "pending")
        .all()
    )

    memories = db.query(UserMemory).all()

    reminders = db.query(Reminder).all()

    return {
        "goal": [
            {
                "key": m.key,
                "value": m.value
            }
            for m in memories
        ],

        "tasks": [
            {
                "id": t.id,
                "title": t.title
            }
            for t in tasks
        ],

        "reminders": [
            {
                "title": r.title,
                "remind_at": r.remind_at
            }
            for r in reminders
        ]
    }