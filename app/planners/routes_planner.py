from flask import Blueprint, request
from app.planners.study_plan_generator import StudyPlanGenerator
from app.kg.neo4j_client import Neo4jClient

bp = Blueprint("planner", __name__)

@bp.route("/study-plan", methods=["GET"])
def study_plan():
    db = Neo4jClient()
    planner = StudyPlanGenerator(db)

    plan = planner.generate()

    return {
        "grade": "Class 10 Science",
        "duration": "June 2026 - March 2027",
        "revisions": 2,
        "plan": plan
    }
