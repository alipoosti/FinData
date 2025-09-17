from fin_data_analysor_agent import FinDataAnalysorAgent

def test_fin_data_analysor_agent_runs():
    agent = FinDataAnalysorAgent()
    output = agent.run("Test_Fin_Doc.md")
    print("Agent output:")
    print(output)

if __name__ == "__main__":
    test_fin_data_analysor_agent_runs()