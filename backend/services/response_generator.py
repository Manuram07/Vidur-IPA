import google.generativeai as genai

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_response(user_message, action_result):

    prompt = f"""
User said:

{user_message}

Action completed:

{action_result}

Reply naturally like a friendly
personal assistant.

Keep response short.
"""

    response = model.generate_content(
        prompt
    )

    return response.text