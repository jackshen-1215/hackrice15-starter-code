import anthropic

from backend.ai.base import LLMProvider
from backend.core.config import settings

class AnthropicClient(LLMProvider):
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    def get_response(self, prompt: str) -> str:
        message = self.client.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="claude-3-5-sonnet-latest",
        )
        return message.content[0].text