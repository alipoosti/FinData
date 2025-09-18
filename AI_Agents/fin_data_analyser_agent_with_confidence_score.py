from typing import List, Dict, Any
import re
import subprocess
import math
import statistics

from .ai_agent_base import BaseAIAgent
from .fin_data_analyser_agent import FinDataAnalyserAgent

class ProfitMarginExtractorAgent(BaseAIAgent):
    """
    Extracts the Profit Margin float from the output text produced by FinDataAnalyserAgent.
    Inherits from BaseAIAgent and returns a float.
    """
    def __init__(self, model_name: str = "llama3.2") -> None:
        system_prompt = (
            "You are a precise data extractor. From the provided text, extract the numeric profit margin "
            "as a percentage value in the range of [0, 100]. Return only the number, without the percentage sign."
        )
        super().__init__(system_prompt=system_prompt, model_name=model_name, temp=0)

    def run(self, input_text: str) -> float:
        """
        Run the extraction using the base agent and parse a float from the output.
        """
        output = super().run(input_text)
        # First try to find a label like "Profit Margin: 12.34" or "Profit Margin = 12.34"
        m = re.search(r"Profit Margin\s*[:=]?\s*(-?\d+(?:\.\d+)?)", output, re.IGNORECASE)
        if m:
            return float(m.group(1))

        # Fallback: extract the first numeric value from the output
        nums = re.findall(r"-?\d+(?:\.\d+)?", output)
        if nums:
            return float(nums[0])

        raise ValueError("Could not extract profit margin from extractor output.")

class FinDataAnalyserAgentWithConfidenceScore:
    """
    Runs FinDataAnalyserAgent multiple times, extracts profit margins, and computes a confidence score.
    The final return is a dict containing:
      - output: the last FinDataAnalyserAgent output
      - margins: list of extracted margins (floats or NaN)
      - confidence_score: a float in [0,1] representing confidence
    """
    def __init__(self, model_name: str = "llama3.2", runs: int = 5) -> None:
        self.model_name = model_name
        self.runs = max(1, int(runs))

    def run(self, fin_doc_path: str) -> Dict[str, Any]:
        outputs: List[str] = []
        # Execute FinDataAnalyserAgent multiple times, clearing Ollama cache between runs
        for _ in range(self.runs):
            agent = FinDataAnalyserAgent(model_name=self.model_name)
            try:
                out = agent.run(fin_doc_path)
            except Exception:
                out = ""
            outputs.append(out)

        extractor = ProfitMarginExtractorAgent(model_name=self.model_name)
        margins: List[float] = []
        for out in outputs:
            try:
                margin = extractor.run(out)
            except Exception:
                margin = float("nan")
            margins.append(margin)

        # Compute confidence score using variance of valid margins
        valid_margins = [m for m in margins if isinstance(m, float) and not math.isnan(m)]
        if len(valid_margins) > 1:
            var = statistics.variance(valid_margins)
        else:
            var = 0.0

        confidence_score = 1.0 if var == 0.0 else 1.0 / (1.0 + var)

        last_output = outputs[-1] if outputs else ""
        return {
            "output": last_output,
            "margins": margins,
            "confidence_score": float(confidence_score),
        }