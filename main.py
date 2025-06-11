from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from yuvasaarthi_bot import YuvaSaarthiBot

app = FastAPI()
bot = YuvaSaarthiBot()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for dev
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    user_input: str
    chat_history: list

@app.post("/chat")
def chat(message: Message):
    return {"response": bot.respond(message.user_input, message.chat_history)}
