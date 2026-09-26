from app import create_app


def test_health():
    client = create_app().test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "ok"
    assert response.json["service"] == "TaxGuardX"


def test_invalid_request():
    client = create_app().test_client()

    response = client.post(
        "/api/analyze",
        json={"amount": 1000}
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "validation_failed"


def test_valid_transaction():
    client = create_app().test_client()

    payload = {
        "transaction_id": "TX-TEST-001",
        "taxpayer_id": "DEMO-001",
        "amount": 1000,
        "country": "IN",
        "expected_country": "IN",
        "failed_attempts": 0,
        "is_duplicate": False,
        "velocity_count": 0
    }

    response = client.post(
        "/api/analyze",
        json=payload
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["transaction_id"] == "TX-TEST-001"
    assert data["risk_score"] == 0
    assert data["risk_level"] == "LOW"
