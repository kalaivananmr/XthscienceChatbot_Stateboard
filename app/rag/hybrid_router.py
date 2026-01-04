def hybrid_search(question, vector_db, graph_db, intent):
    results = {}

    if intent in ["definition", "fill_blank", "explain"]:
        results["vector"] = vector_db.similarity_search(question, k=5)

    if intent in ["chemical", "relation", "chapter_link"]:
        results["graph"] = graph_db.search(question)

    return results
