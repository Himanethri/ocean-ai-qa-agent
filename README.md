Ocean AI – Autonomous QA Agent
An intelligent system that generates test cases and Selenium scripts using FastAPI + Streamlit + RAG.

🚀 Overview

This project builds an Autonomous QA Agent that:

Reads project documents + checkout HTML

Creates a knowledge base using RAG (ChromaDB + Sentence Transformers)

Generates test cases grounded ONLY in documentation

Converts selected test cases into Selenium Python test scripts

Provides a simple Streamlit UI + FastAPI backend

🧩 Tech Stack

FastAPI (Backend)

Streamlit (Frontend UI)

ChromaDB (Vector DB)

Sentence Transformers (Embeddings)

BeautifulSoup, Unstructured, PyMuPDF (Document parsing)

Selenium WebDriver

Python 3.13

📁 Project Structure

Ocean AI Assignment/
│── backend/
│   ├── main.py
│   ├── rag_engine.py
│   ├── testcase_agent.py
│   ├── selenium_agent.py
│── frontend/
│   ├── app.py
│── html/
│   ├── checkout.html
│── documents/
│   ├── product_specs.md
│   ├── ui_ux_guide.txt
│   ├── api_endpoints.json
│── scripts/
│   ├── selenium_script.py
│── README.md

⚙️ Setup Instructions
### 1️⃣ Create Virtual Environment
python -m venv venv

2️⃣ Activate it (Windows)
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt


(or use the installation commands provided)

▶️ How to Run Backend (FastAPI)
uvicorn backend.main:app --reload


Backend opens at:

http://127.0.0.1:8000

▶️ How to Run Frontend (Streamlit UI)

Open new terminal (do NOT close backend):

streamlit run frontend/app.py

✔️ Usage Flow

Upload support documents

Upload checkout.html

Click Build Knowledge Base

Ask for test cases

Select a test case

Generate Selenium script automatically

Copy + Run script in new terminal


📝 Support Documents Explanation

product_specs.md describes functional rules

ui_ux_guide.txt has UI/UX behavior

api_endpoints.json gives API structure

checkout.html is the target web app UI

All test reasoning is grounded strictly in these documents.

👩‍💻 Author

Himanethri