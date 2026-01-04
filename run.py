from flask import Flask
from flask_cors import CORS

# Import blueprints (add more as you build)
from app.api import routes_query
from app.api import routes_ingest
from app.api import routes_graph
from app.api import routes_planner

def create_app():
    """
    Application Factory
    """
    app = Flask(__name__)
    CORS(app)

    # -----------------------------
    # Register API Blueprints
    # -----------------------------
    app.register_blueprint(
        routes_ingest.bp,
        url_prefix="/api/ingest"
    )

    app.register_blueprint(
        routes_query.bp,
        url_prefix="/api/query"
    )

    app.register_blueprint(
        routes_graph.bp,
        url_prefix="/api/graph"
    )

    app.register_blueprint(
        routes_planner.bp,
        url_prefix="/api/planner"
    )

    # -----------------------------
    # Health / Home
    # -----------------------------
    @app.route("/")
    def home():
        return {
            "service": "Science Hybrid RAG API",
            "status": "running"
        }

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
