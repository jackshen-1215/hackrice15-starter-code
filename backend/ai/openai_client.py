from openai import OpenAI

from backend.ai.base import LLMProvider
from backend.core.config import settings

class OpenAIClient(LLMProvider):
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def get_response(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt},
            ],
        )
        return completion.choices[0].message.content