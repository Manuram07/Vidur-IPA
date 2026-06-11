from fastapi import APIRouter
from database.db import SessionLocal

from database.models import (
    Task,
    UserMemory,
    Reminder
)

from schemas.chat_schema import ChatRequest

from services.intent_service import classify_intent
from services.gemini_extractor import extract_information
from services.response_generator import generate_response

router = APIRouter()


@router.post("/assistant")
def assistant(req: ChatRequest):

    db = SessionLocal()

    try:

        result = classify_intent(
            req.message
        )

        intent = result["intent"]

        # =====================
        # MEMORY
        # =====================

        if intent == "memory":

            extracted = extract_information(
                req.message,
                "memory"
            )

            memory = UserMemory(
                key=extracted["key"],
                value=extracted["value"]
            )

            db.add(memory)
            db.commit()

            reply = generate_response(
                req.message,
                f"""
                Memory Saved

                Key:
                {extracted['key']}

                Value:
                {extracted['value']}
                """
            )

            return {
                "intent": "memory",
                "message": reply
            }

        # =====================
        # TASK
        # =====================

        elif intent == "task":

            extracted = extract_information(
                req.message,
                "task"
            )

            task = Task(
                title=extracted["title"],
                status="pending"
            )

            db.add(task)
            db.commit()

            reply = generate_response(
                req.message,
                f"""
                Task Created

                Title:
                {extracted['title']}
                """
            )

            return {
                "intent": "task",
                "message": reply
            }

        # =====================
        # REMINDER
        # =====================

        elif intent == "reminder":

            extracted = extract_information(
                req.message,
                "reminder"
            )

            reminder = Reminder(
                title=extracted["title"],
                remind_at=extracted["date"]
            )

            db.add(reminder)
            db.commit()

            reply = generate_response(
                req.message,
                f"""
                Reminder Created

                Title:
                {extracted['title']}

                Date:
                {extracted['date']}
                """
            )

            return {
                "intent": "reminder",
                "message": reply
            }

        # =====================
        # CHAT
        # =====================

        else:

            reply = generate_response(
                req.message,
                "General Chat"
            )

            return {
                "intent": "chat",
                "message": reply
            }

    except Exception as e:

        return {
            "error": str(e)
        }

    finally:

        db.close()