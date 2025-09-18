from .ai_agent_base import BaseAIAgent


class FinDataAnalyserAgent:
    """
    AI agent that reads a financial document text file and uses a fixed system prompt
    to instruct the base agent to perform a calculation and output an analysis paragraph.
    No NLP or regex extraction is done here; the entire document text is passed as input.
    """

    def __init__(self, model_name: str = "llama3.2") -> None:
        self.system_prompt = (
            "You are an experienced financial analyst. "
            "Read the financial document provided, extract the relevant numbers, "
            "compute the profit margin using the formula: Profit Margin = (NetIncome / Revenue) * 100, "
            "and output a concise paragraph including the calculated number."
        )
        self.base_agent = BaseAIAgent(system_prompt=self.system_prompt, model_name=model_name)

    def run(self, fin_doc_path: str) -> str:
        with open(fin_doc_path, "r", encoding="utf-8") as f:
            fin_doc_text = f.read()

        # Pass the entire document text as input prompt to the base agent
        output = self.base_agent.run(fin_doc_text)
        return output