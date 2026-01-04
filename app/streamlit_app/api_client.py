import requests

API_BASE = "http://localhost:5000/api"

def ask_question(question):
    r = requests.post(
        f"{API_BASE}/query",
        json={"question": question}
    )
    return r.json()

def get_study_plan():
    r = requests.get(f"{API_BASE}/planner/study-plan")
    return r.json()

def ingest_pdf(text):
    r = requests.post(
        f"{API_BASE}/ingest/text",
        json={"text": text}
    )
    return r.json()

def get_graph():
    r = requests.get(f"{API_BASE}/graph/full")
    return r.json()
