from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from backend.rag_engine import RAGEngine
from backend.testcase_agent import generate_test_cases
from backend.selenium_agent import generate_selenium_script


app = FastAPI()

# CORS for Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DOCUMENTS_DIR = "documents/"
HTML_DIR = "html/"

rag = RAGEngine()

@app.post("/upload_docs")
async def upload_docs(files: list[UploadFile]):
    os.makedirs(DOCUMENTS_DIR, exist_ok=True)
    for f in files:
        path = os.path.join(DOCUMENTS_DIR, f.filename)
        with open(path, "wb") as buffer:
            shutil.copyfileobj(f.file, buffer)
    return {"message": "Documents uploaded successfully"}

@app.post("/upload_html")
async def upload_html(file: UploadFile = File(...)):
    os.makedirs(HTML_DIR, exist_ok=True)
    path = os.path.join(HTML_DIR, file.filename)
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "HTML uploaded successfully"}

@app.post("/build_kb")
async def build_kb():
    rag.build_knowledge_base()
    return {"message": "Knowledge Base Built!"}

@app.post("/generate_test_cases")
async def generate_tcs(query: str):
    context = rag.retrieve_context(query)
    tcs = generate_test_cases(query, context)
    return {"testcases": tcs}

@app.post("/generate_script")
async def generate_script(test_case: str):
    html_file = os.path.join(HTML_DIR, "checkout.html")
    with open(html_file, "r", encoding="utf-8") as fp:
        html = fp.read()
    script = generate_selenium_script(test_case, html)
    return {"script": script}

@app.get("/")
def root():
    return {"message": "Backend running OK!"}
