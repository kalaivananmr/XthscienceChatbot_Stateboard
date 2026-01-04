class AccuracyGuard:
    def __init__(self, threshold=0.90):
        self.threshold = threshold

    def is_science_question(self, intent: str) -> bool:
        return intent in [
            "definition",
            "chemical_equation",
            "numerical",
            "fill_blank",
            "explain",
            "diagram",
            "chapter_relation"
        ]

    def is_accurate(self, confidence_score: float) -> bool:
        return confidence_score >= self.threshold

    def decide(
        self,
        confidence_score: float,
        intent: str
    ) -> dict:
        """
        Central decision logic
        """
        if not self.is_accurate(confidence_score):
            if self.is_science_question(intent):
                return {
                    "action": "WEB_SEARCH",
                    "reason": "Low confidence but science-related"
                }
            else:
                return {
                    "action": "ASK_PERMISSION",
                    "reason": "Out of syllabus / non-science"
                }

        return {
            "action": "ANSWER_DIRECTLY",
            "reason": "Confidence acceptable"
        }
