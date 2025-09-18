# FinData Verification and AI Agents

A small project to verify and improve numeric reliability in LLM-driven analysis of financial documents.

## ⚠️ Problem

LLMs often miscalculate or misreport numbers in financial contexts (for example, revenue, net income, or margins), producing confident but incorrect figures.

## 🧩 Approaches

- Approach 1 — Repetition with confidence scoring
  - Run the same task multiple times and report an aggregate answer with a confidence score.
  - Useful to gauge reliability; may still require human review for high-stakes use.
- Approach 2 — Extract-then-calculate using external utilities
  - Use extractor LLM agents to pull the required numbers, then compute with verified Python utilities.
  - Reduces hallucination risk and improves traceability and repeatability.

## 🏗️ Architecture overview

Core agents and utilities:
- [`AI_Agents/fin_data_analyser_agent.py`](AI_Agents/fin_data_analyser_agent.py:1) — agent to read FinDoc and surface needed values.
- [`AI_Agents/fin_data_analyser_agent_with_confidence_score.py`](AI_Agents/fin_data_analyser_agent_with_confidence_score.py:1) — repetition strategy with confidence score.
- [`AI_Agents/fin_data_summarizer.py`](AI_Agents/fin_data_summarizer.py:1) — final report/summary generation based on approach 2.
- [`AI_Agents/ai_agent_base.py`](AI_Agents/ai_agent_base.py:1) — shared base wrapper over LangChain + Ollama.
- [`utils/utility.py`](utils/utility.py:1) — numeric utilities (for example, profit margin).

## 📁 Repository structure

```txt
|- FinData/                          # repository root
|-- README.md
|-- requirements.txt
|-- AI_Agents/
|   |-- __init__.py
|   |-- ai_agent_base.py
|   |-- fin_data_analyser_agent.py
|   |-- fin_data_analyser_agent_with_confidence_score.py
|   |-- fin_data_summarizer.py
|-- utils/
|   |-- __init__.py
|   |-- utility.py
|-- tests/
|   |-- __init__.py
|   |-- Test_Fin_Doc.md
|   |-- Demo_Naive.py
|   |-- Demo_FinDataAnalyserAgentWithConfidenceScore.py
|   |-- Demo_FinDataSummarizer.py
```

## 🚀 Quick start

1) Create and activate a virtual environment

```bash
# Create venv (macOS/Linux)
python3 -m venv .venv
# Activate
source .venv/bin/activate
# Upgrade pip
python -m pip install --upgrade pip
```

2) Install project requirements

```bash
pip install -r requirements.txt
```

3) Ensure Ollama is running with a supported model

- Install and start Ollama: https://ollama.com
- Pull a local model (for example, llama3.2) and ensure it’s available.

## 🧪 Demos: how to run

From the repository root after activating the venv:

```bash
python tests/Demo_Naive.py
python tests/Demo_FinDataAnalyserAgentWithConfidenceScore.py
python tests/Demo_FinDataSummarizer.py
```

Input document used in demos:
- [`tests/Test_Fin_Doc.md`](tests/Test_Fin_Doc.md:1)

```txt
Company: MockTech
Year: 2024
Revenue: 1567000
NetIncome: 398000
Employees: 50
```

The real Profit Margin for this company would be `398000/1567000 = 0.253989`

- Example output of the naive agent (using llama3.1)

  ```txt
  **Financial Analysis Report**

  Based on the provided financial document for MockTech in 2024, I have extracted the relevant numbers and computed the profit margin.

  Relevant Numbers:
  - Revenue: $1,567,000
  - Net Income: $398,000
  - Employees: 50 (not directly used in calculation)

  Using the formula: Profit Margin = (NetIncome / Revenue) * 100

  Profit Margin Calculation:
  = ($398,000 / $1,567,000) * 100
  = 0.2545 * 100
  ≈ 25.45%

  **Conclusion**
  MockTech's profit margin for the year 2024 is approximately 25.45%. This indicates a relatively healthy profitability level, suggesting that MockTech has managed its costs effectively and maintained a strong revenue stream in 2024.
  ```

- Example output of the naive agent (using llama3.2)

  ```txt
  Based on the financial document provided for MockTech in 2024, I extracted the relevant numbers:

  - Revenue: $1,567,000
  - Net Income: $398,000

  Using the formula for profit margin, I calculated it as follows:

  Profit Margin = (NetIncome / Revenue) * 100
  = ($398,000 / $1,567,000) * 100
  = 25.38%

  Therefore, MockTech's profit margin in 2024 is approximately 25.38%.
  ```



## 🧰 Key modules

- [`AI_Agents/ai_agent_base.py`](AI_Agents/ai_agent_base.py:1) — base LLM integration used by all agents.
- [`AI_Agents/fin_data_analyser_agent.py`](AI_Agents/fin_data_analyser_agent.py:1) — main LLM agent for the naive approach.
- [`AI_Agents/fin_data_analyser_agent_with_confidence_score.py`](AI_Agents/fin_data_analyser_agent_with_confidence_score.py:1) — repetition + confidence.
- [`AI_Agents/fin_data_summarizer.py`](AI_Agents/fin_data_summarizer.py:1) — summary/report generation using approach 2.
- [`utils/utility.py`](utils/utility.py:1) — math helpers used to compute verified values.

## 🧱 Test artifacts

- [`tests/Demo_Naive.py`](tests/Demo_Naive.py:1)
- [`tests/Demo_FinDataAnalyserAgentWithConfidenceScore.py`](tests/Demo_FinDataAnalyserAgentWithConfidenceScore.py:1)
- [`tests/Demo_FinDataSummarizer.py`](tests/Demo_FinDataSummarizer.py:1)
- [`tests/Test_Fin_Doc.md`](tests/Test_Fin_Doc.md:1)

## 🔧 Extending

- Add additional FinDoc samples under tests and point demos to them.
- Add new calculators in [`utils/utility.py`](utils/utility.py:1) and wire them into the agents.
- Expand tests and capture outputs in the Example outputs section above.

## 📝 Notes

- Using larger models will reduce the change of miscalculations.
- For production use, prefer the extract-then-calculate approach for numerical reliability.
