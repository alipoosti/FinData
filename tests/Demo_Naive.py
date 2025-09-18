import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from AI_Agents.fin_data_analyser_agent import FinDataAnalyserAgent

def test_fin_data_analyser_agent_runs():
    agent = FinDataAnalyserAgent(model_name="llama3.2")
    output = agent.run("tests/Test_Fin_Doc.md")
    print("Agent output:")
    print(output)

if __name__ == "__main__":
    test_fin_data_analyser_agent_runs()