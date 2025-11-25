import os
import json
import fitz
from unstructured.partition.auto import partition
from sentence_transformers import SentenceTransformer
import chromadb

class RAGEngine:
    def __init__(self):
        self.docs_dir = "documents/"
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection("knowledge_base")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def extract_text(self, filepath):
        ext = filepath.split(".")[-1]

        # Use UNSTRUCTURED for everything except html
        if ext in ["pdf", "md", "txt"]:
            elements = partition(filename=filepath)
            return "\n".join([e.text for e in elements if hasattr(e, "text")])

        # HTML handled manually
        if ext == "html":
            html = open(filepath, "r", encoding="utf-8").read()
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
            return soup.get_text("\n")

        # JSON
        if ext == "json":
            return json.dumps(json.load(open(filepath, "r", encoding="utf-8")), indent=2)

        return ""

    def chunk_text(self, text, size=400):
        words = text.split()
        chunks, curr = [], []
        for w in words:
            curr.append(w)
            if len(curr) >= size:
                chunks.append(" ".join(curr))
                curr = []
        if curr:
            chunks.append(" ".join(curr))
        return chunks

    def build_knowledge_base(self):
        # clear old data
        try:
            self.collection.delete(where={})
        except:
            pass

        for filename in os.listdir(self.docs_dir):
            filepath = os.path.join(self.docs_dir, filename)
            text = self.extract_text(filepath)
            chunks = self.chunk_text(text)

            for i, c in enumerate(chunks):
                emb = self.model.encode(c).tolist()
                self.collection.add(
                    documents=[c],
                    ids=[f"{filename}_{i}"],
                    metadatas=[{"source": filename}],
                    embeddings=[emb]
                )

    def retrieve_context(self, query):
        q_emb = self.model.encode(query).tolist()
        result = self.collection.query(
            query_embeddings=[q_emb],
            n_results=5
        )
        return "\n\n".join(result["documents"][0])
