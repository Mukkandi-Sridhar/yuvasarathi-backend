from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dhraviq_bot import DhraviqBot

app = FastAPI()
bot = DhraviqBot()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class Message(BaseModel):
    user_input: str
    chat_history: list

# Routes
@app.post("/chat")
def chat(message: Message):
    return {"response": bot.respond(message.user_input, message.chat_history)}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/debug")
def debug_check():
    return {"file": "main.py is running"}
