from flask import Blueprint, jsonify, render_template, request

from .risk_engine import analyze_transaction
from .validation import validate_transaction


api = Blueprint("api", __name__)


@api.get("/")
def index():
    return render_template("index.html")


@api.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "TaxGuardX"
    })


@api.post("/api/analyze")
def analyze():
    payload = request.get_json(silent=True)

    if not isinstance(payload, dict):
        return jsonify({
            "error": "JSON object required"
        }), 400

    errors = validate_transaction(payload)

    if errors:
        return jsonify({
            "error": "validation_failed",
            "details": errors
        }), 400

    result = analyze_transaction(payload)

    return jsonify(result)
