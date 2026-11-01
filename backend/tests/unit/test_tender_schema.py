from tenderlens.schemas.tender import Tender


def test_valid_tender():
    tender = Tender(
        title="Road Construction",
        reference_number="TND-2026-001",
        deadline="2026-11-15",
    )

    assert tender.title == "Road Construction"
    assert tender.reference_number == "TND-2026-001"
    assert str(tender.deadline) == "2026-10-15"