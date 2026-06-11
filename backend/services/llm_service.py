import google.generativeai as genai


def classify_intent(message):

    prompt = f"""
You are an intent classifier.

Possible intents:

task
memory
reminder
chat

Examples:

"create a task to learn python"
-> task

"remember my goal is AI engineer"
-> memory

"remind me tomorrow about interview"
-> reminder

"what is machine learning"
-> chat

User:
{message}

Return ONLY ONE WORD.
"""

    response = model.generate_content(prompt)

    return response.text.strip().lower()