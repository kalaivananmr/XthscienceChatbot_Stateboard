from langchain_community.vectorstores import FAISS

def build_vector_store(docs, embeddings, path):
    texts = [d["text"] for d in docs if d["type"] in ["NarrativeText", "ListItem"]]
    metadatas = [d["metadata"] for d in docs if d["type"] in ["NarrativeText", "ListItem"]]

    db = FAISS.from_texts(texts, embeddings, metadatas=metadatas)
    db.save_local(path)
    return db
