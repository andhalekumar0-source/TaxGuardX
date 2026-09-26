from app.risk_engine import analyze_transaction


def base_transaction():
    return {
        "transaction_id": "TX-TEST-001",
        "taxpayer_id": "DEMO-001",
        "amount": 1000,
        "country": "IN",
        "expected_country": "IN",
        "failed_attempts": 0,
        "is_duplicate": False,
        "velocity_count": 0
    }


def test_low_risk_transaction():
    result = analyze_transaction(
        base_transaction()
    )

    assert result["risk_score"] == 0
    assert result["risk_level"] == "LOW"
    assert result["reasons"] == []


def test_large_amount_rule():
    transaction = base_transaction()

    transaction["amount"] = 100000

    result = analyze_transaction(transaction)

    assert result["risk_score"] == 30
    assert result["risk_level"] == "MEDIUM"

    assert result["reasons"][0]["rule"] == "LARGE_AMOUNT"


def test_country_mismatch_rule():
    transaction = base_transaction()

    transaction["country"] = "US"
    transaction["expected_country"] = "IN"

    result = analyze_transaction(transaction)

    assert result["risk_score"] == 25
    assert result["risk_level"] == "LOW"


def test_failed_attempts_rule():
    transaction = base_transaction()

    transaction["failed_attempts"] = 3

    result = analyze_transaction(transaction)

    assert result["risk_score"] == 20
    assert result["risk_level"] == "LOW"


def test_duplicate_rule():
    transaction = base_transaction()

    transaction["is_duplicate"] = True

    result = analyze_transaction(transaction)

    assert result["risk_score"] == 25
    assert result["risk_level"] == "LOW"


def test_high_velocity_rule():
    transaction = base_transaction()

    transaction["velocity_count"] = 10

    result = analyze_transaction(transaction)

    assert result["risk_score"] == 20
    assert result["risk_level"] == "LOW"


def test_high_risk_combination():
    transaction = base_transaction()

    transaction["amount"] = 150000
    transaction["country"] = "US"
    transaction["expected_country"] = "IN"
    transaction["failed_attempts"] = 3
    transaction["is_duplicate"] = True

    result = analyze_transaction(transaction)

    assert result["risk_score"] == 100
    assert result["risk_level"] == "HIGH"

    assert len(result["reasons"]) == 4
