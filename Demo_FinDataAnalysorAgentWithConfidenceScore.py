import sys

def main():
    try:
        from FinDataAnalysorAgentWithConfidenceScore import FinDataAnalysorAgentWithConfidenceScore
        agent = FinDataAnalysorAgentWithConfidenceScore(model_name= "llama3.1", runs=5)
        result = agent.run("Test_Fin_Doc.md")
        print("Demo Result (FinDataAnalysorAgentWithConfidenceScore):\n\n")
        print(f"output: {result['output']}\n\n")
        print(f"margins: {result['margins']}\n\n")
        print(f"confidence_score: {result['confidence_score']}")

    except Exception as e:
        print("Demo failed:", e)

if __name__ == "__main__":
    main()