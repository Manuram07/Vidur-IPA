import json
import google.generativeai as genai

genai.configure(
    api_key="YOUR_GEMINI_API_KEY"
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def extract_information(message, intent):

    prompt = f"""
You are an information extraction engine.

User Message:
{message}

Intent:
{intent}

Return ONLY valid JSON.

For memory:
{{
  "key": "",
  "value": ""
}}

For task:
{{
  "title": ""
}}

For reminder:
{{
  "title": "",
  "date": ""
}}

No explanations.
No markdown.
Only JSON.
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    return json.loads(text)