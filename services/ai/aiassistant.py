from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import g4f
from g4f import typing as g4ftype

class AiAssistant:
    def __init__(self):
        print("Ai Assistant initalized")
    def get_single_response(self, content: str) -> str:
        message = g4ftype.Message(role="user", content=content)
        try:
            gpt_response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_4,
                messages=[message],
            )
        except Exception as e:
            raise RuntimeError(f"Error while getting response: {e}")
        return gpt_response

app = FastAPI()
assistant = AiAssistant()

class AskRequest(BaseModel):
    prompt: str

class AskResponse(BaseModel):
    response: str

@app.post("/ask", response_model=AskResponse)
async def ask_endpoint(req: AskRequest):
    try:
        ai_response = assistant.get_single_response(req.prompt)
        return AskResponse(response=ai_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
