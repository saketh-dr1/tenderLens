def validate_tender(tender: dict) -> list[str]:
    required_fields = ["title", "reference_number", "deadline"]
    errors = []

    for field in required_fields:
        if field not in tender:
            errors.append(f"Missing field: {field}")
        elif not isinstance(tender[field], str) or not tender[field].strip():
            errors.append(f"Invalid or empty field: {field}")

    return errors


def display_tender(tender: dict) -> None:
    errors = validate_tender(tender)

    if errors:
        print("Invalid tender:")
        for error in errors:
            print(f"- {error}")
        return

    print(f"Tender Title: {tender['title']}")
    print(f"Reference Number: {tender['reference_number']}")
    print(f"Submission Deadline: {tender['deadline']}")


def main() -> None:
    tender = {
        "title": "Road Construction",
        "reference_number": "TND-2026-001",
        "deadline": "2026-11-15",
    }

    display_tender(tender)