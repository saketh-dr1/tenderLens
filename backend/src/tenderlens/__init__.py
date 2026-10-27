
def display_tender(tender:dict) -> None:
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