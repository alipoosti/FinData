from AI_Agents.ai_agent_base import BaseAIAgent
from utils.utility import calculate_profit_margin


class NetIncomeExtractorAgent:
    def __init__(self, model_name: str = "llama3.2") -> None:
        self.system_prompt = (
            "You are an experienced financial data extractor. Given a text containing financial statements, "
            "output only the Net Income value reported in the document. Output should be a number with no currency "
            "symbol or extra text."
        )
        self.base_agent = BaseAIAgent(system_prompt=self.system_prompt, model_name=model_name)

    def run(self, text: str) -> float:
        output = self.base_agent.run(text)
        if output is None:
            return 0.0
        s = str(output).strip()
        # Try direct float conversion
        try:
            return float(s)
        except ValueError:
            import re
            m = re.search(r"-?\d+(?:\.\d+)?", s)
            if m:
                try:
                    return float(m.group(0))
                except ValueError:
                    pass
        return 0.0


class RevenueExtractorAgent:
    def __init__(self, model_name: str = "llama3.2") -> None:
        self.system_prompt = (
            "You are an experienced financial data extractor. Given a text containing financial statements, "
            "output only the Revenue value reported in the document. Output should be a number with no currency "
            "symbol or extra text."
        )
        self.base_agent = BaseAIAgent(system_prompt=self.system_prompt, model_name=model_name)

    def run(self, text: str) -> float:
        output = self.base_agent.run(text)
        if output is None:
            return 0.0
        s = str(output).strip()
        # Try direct float conversion
        try:
            return float(s)
        except ValueError:
            import re
            m = re.search(r"-?\d+(?:\.\d+)?", s)
            if m:
                try:
                    return float(m.group(0))
                except ValueError:
                    pass
        return 0.0


class FinDataSummarizerAgent:
    def __init__(self, model_name: str = "llama3.2") -> None:
        self.net_income_extractor = NetIncomeExtractorAgent(model_name=model_name)
        self.revenue_extractor = RevenueExtractorAgent(model_name=model_name)
        self.system_prompt = (
            "You are an experienced financial analyst. Read the financial document text provided and "
            "produce a concise, informative summary of the company based on the document."
        )
        self.base_agent = BaseAIAgent(system_prompt=self.system_prompt, model_name=model_name)

    def run(self, fin_doc_path: str) -> str:
        with open(fin_doc_path, "r", encoding="utf-8") as f:
            fin_doc_text = f.read()

        net_income = self.net_income_extractor.run(fin_doc_text)
        # print(f"NetIncome extracted as {net_income}")
        revenue = self.revenue_extractor.run(fin_doc_text)
        # print(f"Rev extracted as {revenue}")
        profit_margin = calculate_profit_margin(net_income, revenue)

        summary = self.base_agent.run(fin_doc_text)
        final_summary = summary.strip()
        final_summary = final_summary
        final_summary = final_summary + "\n\n" + f"**Profit Margin** \nGiven the net income and revenue of the company the Profit Margin is calculated at: {profit_margin:.3f}%.\nThis metric shows how efficiently the company converts revenue into profit, representing net income as a percentage of revenue."
        return final_summary