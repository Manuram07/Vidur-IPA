from fastapi import APIRouter
from database.db import SessionLocal
from database.models import Reminder
from schemas.reminder_schema import ReminderCreate

router = APIRouter()

@router.post("/reminder")
def create_reminder(reminder: ReminderCreate):

    db = SessionLocal()

    new_reminder = Reminder(
        title=reminder.title,
        remind_at=reminder.remind_at
    )

    db.add(new_reminder)
    db.commit()

    return {
        "message": "Reminder created"
    }


@router.get("/reminders")
def get_reminders():

    db = SessionLocal()

    return db.query(Reminder).all()