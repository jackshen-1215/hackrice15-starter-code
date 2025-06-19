from abc import ABC, abstractmethod

class LLMProvider(ABC):
    @abstractmethod
    def get_response(self, prompt: str) -> str:
        pass