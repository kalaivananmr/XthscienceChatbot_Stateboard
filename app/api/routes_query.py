from app.core.accuracy_guard import AccuracyGuard
from app.web.web_search import web_search

accuracy_guard = AccuracyGuard()

@bp.route("/query", methods=["POST"])
def query():
    payload = request.json
    question = payload["question"]

    # 1. Classify intent
    intent = classify_question(question)

    # 2. Retrieve context
    context, sources = hybrid_retrieve(question, intent)

    # 3. Generate answer
    answer = generate_answer(question, context)

    # 4. Confidence score
    confidence = compute_confidence(answer, sources)

    # 5. Accuracy decision
    decision = accuracy_guard.decide(confidence, intent)

    if decision["action"] == "ANSWER_DIRECTLY":
        return {
            "answer": answer,
            "confidence": confidence,
            "source": "PDF / Knowledge Graph"
        }

    if decision["action"] == "WEB_SEARCH":
        web_answer = web_search(question)
        return {
            "answer": web_answer,
            "confidence": confidence,
            "source": "Web (fallback)",
            "note": "Used web due to low confidence"
        }

    if decision["action"] == "ASK_PERMISSION":
        return {
            "message": (
                "This question is not directly related to the science textbook. "
                "Do you want me to search the web?"
            ),
            "options": ["Allow", "Not Allow"]
        }
