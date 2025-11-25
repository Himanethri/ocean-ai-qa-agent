import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Autonomous QA Agent", layout="wide")
st.title("🧠 Autonomous QA Agent for Test Cases & Selenium Scripts")

# --------------------------------------
# Upload Documents
# --------------------------------------
st.header("1️⃣ Upload Support Documents")
docs = st.file_uploader("Upload 3–5 support documents", accept_multiple_files=True)

if st.button("Upload Documents"):
    if docs:
        files = [("files", (f.name, f, f.type)) for f in docs]
        res = requests.post(f"{BACKEND_URL}/upload_docs", files=files)
        st.success(res.json()["message"])
    else:
        st.warning("Please upload at least one document.")

st.divider()

# --------------------------------------
# Upload HTML
# --------------------------------------
st.header("2️⃣ Upload checkout.html")
html_file = st.file_uploader("Upload checkout.html", type=["html"])

if st.button("Upload HTML File"):
    if html_file:
        res = requests.post(
            f"{BACKEND_URL}/upload_html",
            files={"file": (html_file.name, html_file, html_file.type)},
        )
        st.success(res.json()["message"])
    else:
        st.warning("Upload checkout.html!")

st.divider()

# --------------------------------------
# Build KB
# --------------------------------------
st.header("3️⃣ Build Knowledge Base")

if st.button("Build Knowledge Base"):
    res = requests.post(f"{BACKEND_URL}/build_kb")
    st.success(res.json()["message"])

st.divider()

# --------------------------------------
# Generate Test Cases
# --------------------------------------
st.header("4️⃣ Generate Test Cases")
query = st.text_input("Describe the feature to test (Example: 'Generate all tests for discount code')")

if st.button("Generate Test Cases"):
    if query:
        res = requests.post(f"{BACKEND_URL}/generate_test_cases", params={"query": query})
        st.markdown(res.json()["testcases"])
    else:
        st.warning("Please enter a query.")

st.divider()

# --------------------------------------
# Generate Selenium Script
# --------------------------------------
st.header("5️⃣ Generate Selenium Script")

test_case_text = st.text_area("Paste one generated test case here")

if st.button("Generate Selenium Script"):
    if test_case_text:
        res = requests.post(f"{BACKEND_URL}/generate_script", params={"test_case": test_case_text})
        st.code(res.json()["script"], language="python")
    else:
        st.warning("Paste a test case first!")

