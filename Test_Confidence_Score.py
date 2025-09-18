import re
import importlib

# Demo approach: monkeypatch internal classes to avoid needing external LLMs.

import FinDataAnalysorAgentWithConfidenceScore as F

# Sequence of fake FinDataAnalysorAgent outputs (as if they came from 5 runs)
fake_outputs = [
    "Profit Margin: 10.0",
    "Profit Margin: 12.0",
    "Profit Margin: 11.5",
    "Profit Margin: 9.5",
    "Profit Margin: 10.5",
]

class FakeFinDataAnalysorAgent:
    def __init__(self, model_name="llama3.2"):
        pass
    def run(self, fin_doc_path: str) -> str:
        return fake_outputs.pop(0) if fake_outputs else ""

class FakeProfitMarginExtractorAgent:
    def __init__(self, model_name="llama3.2"):
        pass
    def run(self, input_text: str) -> float:
        m = re.findall(r"-?\d+(?:\.\d+)?", input_text)
        if m:
            return float(m[0])
        return 0.0

# Patch module globals so the higher-level agent uses the fake components
F.FinDataAnalysorAgent = FakeFinDataAnalysorAgent
F.ProfitMarginExtractorAgent = FakeProfitMarginExtractorAgent

def main():
    agent = F.FinDataAnalysorAgentWithConfidenceScore(runs=5)
    result = agent.run("dummy_path")
    print("Result:", result)

if __name__ == "__main__":
    main()