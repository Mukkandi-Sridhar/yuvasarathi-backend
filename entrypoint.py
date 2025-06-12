from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dhraviq_bot import DhraviqBot

print("✅ entrypoint.py has started.")

app = FastAPI()
bot = DhraviqBot()

# CORS middleware
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

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/debug")
def debug_check():
    print("✅ /debug route called.")
    return {"file": "entrypoint.py is running"}
