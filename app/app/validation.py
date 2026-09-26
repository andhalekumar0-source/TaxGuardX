REQUIRED_FIELDS = [
    "transaction_id",
    "taxpayer_id",
    "amount",
    "country",
    "expected_country",
]


def validate_transaction(data):
    errors = []

    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"missing field: {field}")

    if "amount" in data:
        try:
            amount = float(data["amount"])

            if amount < 0:
                errors.append("amount must be non-negative")

        except (TypeError, ValueError):
            errors.append("amount must be numeric")

    for field in ("country", "expected_country"):
        if field in data and not isinstance(data[field], str):
            errors.append(f"{field} must be a string")

    if "failed_attempts" in data:
        try:
            if int(data["failed_attempts"]) < 0:
                errors.append("failed_attempts must be non-negative")
        except (TypeError, ValueError):
            errors.append("failed_attempts must be an integer")

    return errors
