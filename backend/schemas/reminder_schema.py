from pydantic import BaseModel

class ReminderCreate(BaseModel):
    title: str
    remind_at: str