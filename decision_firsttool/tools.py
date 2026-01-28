notes = []

def save_note(text: str):
    notes.append(text)
    return "Note saved successfully."

def get_notes():
    return notes

def set_reminder(task: str):
    return f"Reminder set for: {task}"
