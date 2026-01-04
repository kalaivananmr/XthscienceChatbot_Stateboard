from datetime import date
from collections import defaultdict

class StudyPlanGenerator:
    """
    Generates a chapter-wise, exam-aligned study plan
    using Knowledge Graph data.
    """

    def __init__(self, neo4j_client):
        self.db = neo4j_client

    def get_chapters_with_difficulty(self):
        """
        Pulls chapter name and difficulty from KG
        """
        query = """
        MATCH (c:Chapter)
        RETURN c.name AS name,
               coalesce(c.difficulty, 2) AS difficulty,
               c.number AS number
        ORDER BY c.number
        """
        return self.db.run(query)

    def get_exam_calendar(self):
        """
        Static but configurable exam schedule
        """
        return {
            "Quarterly": "September",
            "Half-Yearly": "December",
            "Board": "March"
        }

    def generate(self):
        chapters = self.get_chapters_with_difficulty()
        exams = self.get_exam_calendar()

        months = [
            "June", "July", "August",
            "September", "October", "November",
            "December", "January", "February", "March"
        ]

        plan = defaultdict(list)

        # Sort chapters by difficulty (harder earlier)
        chapters = sorted(chapters, key=lambda x: (-x["difficulty"], x["number"]))

        chapter_index = 0

        for month in months:
            # Revision months
            if month in ["January", "February"]:
                plan[month].append({
                    "type": "Revision",
                    "chapters": "All completed chapters",
                    "tests": "Full syllabus test"
                })
                continue

            # Board exam month
            if month == "March":
                plan[month].append({
                    "type": "Final Revision",
                    "chapters": "Entire syllabus",
                    "tests": "Board model papers"
                })
                continue

            # Learning months
            monthly_chapters = chapters[chapter_index:chapter_index + 2]
            chapter_index += 2

            plan[month].append({
                "type": "Learning",
                "chapters": [c["name"] for c in monthly_chapters],
                "tests": self._exam_if_any(month, exams)
            })

        return dict(plan)

    def _exam_if_any(self, month, exams):
        for exam, exam_month in exams.items():
            if exam_month == month:
                return f"{exam} Exam"
        return "Weekly Tests"
