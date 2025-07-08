from backend.ai.base import LLMProvider
from backend.ai.openai_client import OpenAIClient
from backend.ai.anthropic_client import AnthropicClient
from backend.ai.gemini_client import GeminiClient

def get_llm_provider(provider_name: str) -> LLMProvider:
    if provider_name == "openai":
        return OpenAIClient()
    elif provider_name == "anthropic":
        return AnthropicClient()
    elif provider_name == "gemini":
        return GeminiClient()
    # Add other providers here
    # elif provider_name == "deepseek":
    #     return DeepSeekClient()
    # elif provider_name == "llama":
    #     return LLaMaClient()
    else:
        raise ValueError(f"Unknown LLM provider: {provider_name}")