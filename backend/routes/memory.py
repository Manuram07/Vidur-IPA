from fastapi import APIRouter
from database.db import SessionLocal
from database.models import UserMemory
from schemas.memory_schema import MemoryCreate

router = APIRouter()

@router.post("/memory")
def save_memory(memory: MemoryCreate):

    db = SessionLocal()

    new_memory = UserMemory(
        key=memory.key,
        value=memory.value
    )

    db.add(new_memory)
    db.commit()

    return {
        "message": "Memory saved"
    }

@router.get("/memory")
def get_memory():

    db = SessionLocal()

    memories = db.query(UserMemory).all()

    return memories

@router.get("/memory/{key}")
def get_memory_by_key(key: str):

    db = SessionLocal()

    memory = (
        db.query(UserMemory)
        .filter(UserMemory.key == key)
        .first()
    )

    if not memory:
        return {
            "error": "Not found"
        }

    return memory

@router.put("/memory/{key}")
def update_memory(key: str, value: str):

    db = SessionLocal()

    memory = (
        db.query(UserMemory)
        .filter(UserMemory.key == key)
        .first()
    )

    if not memory:
        return {
            "error": "Not found"
        }

    memory.value = value

    db.commit()

    return {
        "message": "Updated"
    }