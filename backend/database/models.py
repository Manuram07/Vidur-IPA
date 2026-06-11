from sqlalchemy import Column, Integer, String
from database.db import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String)
    content = Column(String)

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    status = Column(String, default="pending")

class UserMemory(Base):

    __tablename__ = "user_memory"

    id = Column(Integer, primary_key=True, index=True)

    key = Column(String)

    value = Column(String)

class Reminder(Base):

    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    remind_at = Column(String)