import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from AI_Agents.fin_data_analyser_agent_with_confidence_score import FinDataAnalyserAgentWithConfidenceScore

def main():
    try:
        agent = FinDataAnalyserAgentWithConfidenceScore(model_name= "llama3.1", runs=5)
        result = agent.run("tests/Test_Fin_Doc.md")
        print("Demo Result (FinDataAnalyserAgentWithConfidenceScore):\n\n")
        print(f"output: {result['output']}\n\n")
        print(f"margins: {result['margins']}\n\n")
        print(f"confidence_score: {result['confidence_score']}")

    except Exception as e:
        print("Demo failed:", e)

if __name__ == "__main__":
    main()