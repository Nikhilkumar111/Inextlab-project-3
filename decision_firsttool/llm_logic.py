# llm_logic.py

from gemini_client import call_gemini
import json
import re


def extract_json(text: str):
    """
    Extract JSON object from Gemini response
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group(0) if match else None


def llm_decision(message: str):
    prompt = f"""
You are a tool-calling assistant.

Available tools:
1. save_note → saves a note (argument: text)
2. get_notes → returns all notes (no arguments)
3. set_reminder → sets a reminder (argument: task)

Rules:
- Respond ONLY with valid JSON
- Do not include markdown or extra text
- If no tool is required, use tool as "none"

JSON format:
{{
  "explanation": "string",
  "tool": "save_note | get_notes | set_reminder | none",
  "arguments": {{}}
}}

User message:
"{message}"
"""

    raw_output = call_gemini(prompt)

    json_text = extract_json(raw_output)

    if not json_text:
        return {
            "explanation": "Unable to interpret the request",
            "tool": "none",
            "arguments": {}
        }

    try:
        return json.loads(json_text)
    except Exception:
        return {
            "explanation": "Invalid JSON returned by LLM",
            "tool": "none",
            "arguments": {}
        }
