# Verification of FinData - Phase 1 Plan

This repository documents the first phase plan to test and verify FinData data processed by LLMs. It focuses on building a mock AI agent that reads a FinDoc text and performs a simple calculation using data from the doc. The agent runs locally with LangChain and Ollama models.

## Goals

- Create a self-contained README based plan with test Fin Doc data
- Provide a skeleton of Python modules for AI agents that use a local Ollama model
- Define a fixed system prompt based agent that outputs a paragraph including a calculated number
- Provide an end-to-end test harness concept for repeated runs and variance detection
- Add a utility function for profit margin calculation for later validation phases

## Test Fin Doc (mock)

- Below is a sample Fin Doc that the agent will read. It is included as a snippet in this README for simplicity.

```txt
Company: MockTech
Year: 2024
Revenue: 1500000
NetIncome: 300000
Employees: 50
```

- Simple calculation: Profit Margin = (NetIncome / Revenue) * 100

- Expected result in the paragraph: roughly 20.0%

## AI Agent architecture (high level)

- `ai_agent_base.py`: Base AI agent class using LangChain Ollama LLM (default model llama3.2). It takes a system prompt and an input prompt string, calls the Ollama model, and returns the output.
- `fin_data_analysor_agent.py`: `FinDataAnalysorAgent` reads a financial document text file, uses a fixed system prompt explaining the task and formula, and calls the base agent with the entire document text as input. It returns the output paragraph. No NLP or regex extraction is done here (reserved for later phases).
- `utility.py`: Contains a simple utility function `calculate_profit_margin(net_income, revenue)` that returns the profit margin percentage. This will be used in later phases for validation.

## Testing

- `Test_Naive.py`: A simple test script that instantiates the `FinDataAnalysorAgent` and runs it on the sample `Test_Fin_Doc.md` file to verify it executes without errors and produces output.

## How to run

1. Ensure Ollama is installed and running locally with the llama3.2 model.
2. Run `Test_Naive.py` to verify the agent runs and produces output.
3. Extend or modify the financial document and observe the agent's output paragraph.

## Next steps (overview)

1. Implement multiple runs of the agent to collect output variance and confidence scores.
2. Use NLP and regex techniques to extract numbers from the document, perform math in Python using the utility function, and pass the calculated number to a second agent for paragraph generation.
3. Extend test data and measure error magnitudes and detection.

## Setup and prerequisites

- macOS with Ollama installed
- Python 3.8+
- LangChain installed (`%pip install -qU langchain-ollama`)
- Ollama server running locally and accessible by LangChain
- Local LLM model installed in Ollama (e.g., llama3.2)

## File overview

- `ai_agent_base.py`: Base AI agent class wrapping LangChain Ollama calls.
- `fin_data_analysor_agent.py`: Fixed prompt agent reading Fin Doc and calling base agent.
- `utility.py`: Simple profit margin calculation utility function.
- `Test_Naive.py`: Basic test script to run the FinDataAnalysorAgent on sample data.
