import google.generativeai as genai

from backend.ai.base import LLMProvider
from backend.core.config import settings

class GeminiClient(LLMProvider):
    def __init__(self):
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def get_response(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text