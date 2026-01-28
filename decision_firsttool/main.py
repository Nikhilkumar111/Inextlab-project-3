from fastapi import FastAPI
from schemas import ChatRequest
from llm_logic import llm_decision
import tools

app = FastAPI()

@app.post("/chat")
def chat(request: ChatRequest):
    decision = llm_decision(request.message)

    if decision["tool"] == "save_note":
        result = tools.save_note(**decision["arguments"])
    elif decision["tool"] == "get_notes":
        result = tools.get_notes()
    elif decision["tool"] == "set_reminder":
        result = tools.set_reminder(**decision["arguments"])
    else:
        result = "No tool executed."

    return {
        "explanation": decision.get("explanation"),
        "result": result
    }



# Query 1.
# step 1
# {
#   "message": "Save note: Finish FastAPI tool calling project"
# }


# step 2

# {
#   "message": "Show my notes"
# }

# step 3

# {
#   "message": "Explain what tool calling is"
# }




