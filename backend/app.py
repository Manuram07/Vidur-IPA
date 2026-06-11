from fastapi import APIRouter
from database.db import SessionLocal
from database.models import Task
from schemas.task_schema import TaskCreate
from schemas.task_schema import TaskResponse
from fastapi import FastAPI
from dotenv import load_dotenv
import google.generativeai as genai
import os
from routes.tasks import router as task_router
from database.db import engine
from database.db import SessionLocal
from database.models import Base
from database.models import Message
from routes.memory import router as memory_router
from schemas.chat_schema import ChatRequest
from schemas.chat_schema import ChatResponse
from routes.reminders import router as reminder_router
from routes.planner import router as planner_router
from services.llm_service import classify_intent
from routes.assistant import router as assistant_router
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)
Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Personal Assistant API"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(planner_router)
app.include_router(task_router)
app.include_router(memory_router) 
app.include_router(reminder_router)
app.include_router(assistant_router)


@app.get("/")
def home():
    return {
        "message": "Personal Assistant Running"
    }


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


from typing import List

@router.get(
    "/tasks",
    response_model=List[TaskResponse]
)
def get_tasks():

    db = SessionLocal()

    return db.query(Task).all()

@router.get("/memory")
def get_memory():

    db = SessionLocal()

    memories = db.query(UserMemory).all()

    return memories