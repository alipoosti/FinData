from typing import Optional
from langchain_ollama import ChatOllama


class BaseAIAgent:
    """
    Generic AI agent using LangChain Ollama LLM.

    Attributes:
        model_name (str): Ollama model name to use (default llama3.2).
        system_prompt (str): System prompt string to guide the LLM.
    """

    def __init__(self, system_prompt: str, model_name: str = "llama3.2") -> None:
        self.model_name = model_name
        self.system_prompt = system_prompt
        self.llm = ChatOllama(model=self.model_name, temperature=0)

    def run(self, input_prompt: str) -> str:
        """
        Runs the LLM with the combined system prompt and input prompt.

        Args:
            input_prompt (str): The user input prompt string.

        Returns:
            str: The LLM output string.
        """
        full_prompt = f"System: {self.system_prompt}\nUser: {input_prompt}"
        messages = [
            ("system", self.system_prompt),
            ("human", input_prompt),
        ]
        try:
            ai_msg = self.llm.invoke(messages)
        except Exception as e:
            # Handle model not found error gracefully
            if 'model' in str(e).lower() and 'not found' in str(e).lower():
                raise RuntimeError(f"Model '{self.model_name}' not found on the system. Please pull the model first.") from e
            else:
                raise
        return ai_msg.content