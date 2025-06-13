from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dhraviq_bot import DhraviqBot

app = FastAPI()
bot = DhraviqBot()

# Enable CORS for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    user_input: str
    chat_history: list

@app.post("/chat")
def chat(message: Message):
    return {"response": bot.respond(message.user_input, message.chat_history)}

# ✅ Allow both GET and HEAD for health check
@app.api_route("/health", methods=["GET", "HEAD"])
def health_check():
    return {"status": "ok"}

@app.get("/debug")
def debug():
    return {"status": "main.py is running"}
