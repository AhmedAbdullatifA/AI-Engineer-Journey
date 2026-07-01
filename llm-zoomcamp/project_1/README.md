Markdown
# ⚽ Premier League 2025-2026 AI Analyst

A lightweight Python web application that acts as an expert football analyst. It utilizes **Groq API** with the **Llama 3.1** model to answer contextual questions about the final standings of the English Premier League for the 2025-2026 season via a modern web interface.

This project is a practical application built as part of the **LLM Zoomcamp by DataTalksClub**.

---

## 🚀 Features
- **Interactive Web UI:** Built with **Streamlit** for a clean, responsive, and user-friendly dark-themed interface.

- **Context-Aware QA:** Uses Prompt Engineering to supply a full dataset (League Table) as context to the LLM.

- **Ultra Fast Inference:** Powered by Groq Cloud API (`llama-3.1-8b-instant`).

- **Modern Package Management:** Built and managed using `uv` for lightning-fast dependency loading.

- **Secure Credentials:** Keeps API keys secure using environment variables (`python-dotenv`).

---

## 🛠️ Project Structure
```text
├── pl-2026.py     # Main Streamlit web application script
└── README.md          # Documentation
└── Screen_1.png       # Picture of model

⚙️ Installation & Setup
1. Prerequisites
Make sure you have uv installed. If not, install it via:
pip install uv

2. Clone & Navigate
git clone <your-repository-url>
cd <repository-folder>

3. Environment Setup
Create a .env file in the root directory:

GROQ_API_KEY="your_actual_groq_api_key"
GROQ_API_BASE_URL="[https://api.groq.com/openai/v1](https://api.groq.com/openai/v1)"

💻 How to Run
Use uv run to safely launch the Streamlit server within your virtual environment:
uv run streamlit run pl-2026.py

Alternatively, you can run it using standard Python:
python -m streamlit run pl-2026.py