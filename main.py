from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dhraviq_bot import DhraviqBot  # updated import

print("✅ main.py has started.")  # Debug to confirm this file is loaded

app = FastAPI()
bot = DhraviqBot()  # updated instance

# CORS middleware for frontend/backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development)
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body schema
class Message(BaseModel):
    user_input: str
    chat_history: list

# Chat endpoint
@app.post("/chat")
def chat(message: Message):
    return {"response": bot.respond(message.user_input, message.chat_history)}

# ✅ Health check endpoint to keep Render backend warm
@app.get("/health")
def health_check():
    return {"status": "ok"}

# ✅ Debug route to confirm main.py is running
@app.get("/debug")
def debug_check():
    print("✅ /debug route called.")  # Log when this route is triggered
    return {"file": "main.py is running"}
