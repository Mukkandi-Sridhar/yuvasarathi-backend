import re
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class DhraviqBot:
    def __init__(self):
        self.name = "Dhraviq"
        self.system_prompt = self._get_system_prompt()
        self.model = genai.GenerativeModel("gemini-1.5-pro")
        self.chat_session = self.model.start_chat(history=[])
        self.memory = []

    def _get_system_prompt(self):
        return '''
You are Dhraviq — a multi-agent AI mentor for Tier-3 students...
(Insert your full prompt here, tailored to Dhraviq’s character)
'''

    def respond(self, user_input, chat_history):
        self.memory.append({"user": user_input})
        memory_context = ""
        for item in self.memory[-6:]:
            if "user" in item:
                memory_context += f"👤 User: {item['user']}\n"
            elif "bot" in item:
                memory_context += f"🤖 Dhraviq: {item['bot']}\n"
        full_prompt = f"{self.system_prompt}\n--- MEMORY CONTEXT ---\n{memory_context}\n--- CURRENT QUESTION ---\n{user_input}"
        try:
            response = self.chat_session.send_message(full_prompt)
            reply = response.text
            reply = re.sub(r"\bI am\b", "Dhraviq is", reply)
            reply = re.sub(r"\bmy\b", "Dhraviq's", reply)
            self.memory.append({"bot": reply})
            return reply
        except Exception as e:
            return f"⚠️ Error: {e}"
