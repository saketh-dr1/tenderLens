from tenderlens import validate_tender


def test_valid_tender():
    tender = {
        "title": "Road Construction",
        "reference_number": "TND-2026-001",
        "deadline": "2026-11-15",
    }

    errors = validate_tender(tender)

    assert errors == []


def test_missing_title():
    tender = {
        "reference_number": "TND-2026-001",
        "deadline": "2026-11-15",
    }

    errors = validate_tender(tender)

    assert "Missing field: title" in errors


def test_empty_title():
    tender = {
        "title": "",
        "reference_number": "TND-2026-001",
        "deadline": "2026-11-15",
    }

    errors = validate_tender(tender)

    assert "Invalid or empty field: title" in errors


def test_whitespace_title():
    tender = {
        "title": "   ",
        "reference_number": "TND-2026-001",
        "deadline": "2026-11-15",
    }

    errors = validate_tender(tender)

    assert "Invalid or empty field: title" in errors

def test_none_input():
    errors = validate_tender(None)

    assert errors == ["Invalid input: tender must be a dictionary"]

def test_string_input():
    errors = validate_tender("Road Construction")

    assert errors == ["Invalid input: tender must be a dictionary"]


def test_list_input():
    errors = validate_tender([])

    assert errors == ["Invalid input: tender must be a dictionary"]