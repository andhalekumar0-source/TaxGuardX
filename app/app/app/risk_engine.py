def analyze_transaction(tx):
    amount = float(tx.get("amount", 0))
    failed = int(tx.get("failed_attempts", 0))
    duplicate = bool(tx.get("is_duplicate", False))
    velocity = int(tx.get("velocity_count", 0))

    country_mismatch = (
        tx.get("country") != tx.get("expected_country")
    )

    score = 0
    reasons = []

    if amount >= 100000:
        score += 30
        reasons.append({
            "rule": "LARGE_AMOUNT",
            "points": 30,
            "message": "Transaction amount exceeds the demo threshold."
        })

    if country_mismatch:
        score += 25
        reasons.append({
            "rule": "COUNTRY_MISMATCH",
            "points": 25,
            "message": "Transaction country differs from expected country."
        })

    if failed >= 3:
        score += 20
        reasons.append({
            "rule": "FAILED_ATTEMPTS",
            "points": 20,
            "message": "Multiple failed attempts were reported."
        })

    if duplicate:
        score += 25
        reasons.append({
            "rule": "DUPLICATE_TRANSACTION",
            "points": 25,
            "message": "The transaction is marked as a duplicate."
        })

    if velocity >= 10:
        score += 20
        reasons.append({
            "rule": "HIGH_VELOCITY",
            "points": 20,
            "message": "Transaction velocity exceeds the demo threshold."
        })

    if score >= 60:
        risk = "HIGH"
    elif score >= 30:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "transaction_id": tx["transaction_id"],
        "risk_score": score,
        "risk_level": risk,
        "reasons": reasons
    }
