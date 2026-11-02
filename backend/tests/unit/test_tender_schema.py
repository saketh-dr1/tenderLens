import pytest
from pydantic import ValidationError

from tenderlens.schemas.tender import Tender


@pytest.mark.parametrize("title", ["", " ", "   ", "\t", "\n"])
def test_invalid_title(title):
    with pytest.raises(ValidationError):
        Tender(
            title=title,
            reference_number="TND-2026-001",
            deadline="2026-11-15",
        )


def test_title_whitespace_is_normalized():
    tender = Tender(
        title="  Road Construction  ",
        reference_number="TND-2026-001",
        deadline="2026-11-15",
    )

    assert tender.title == "Road Construction"


def test_invalid_reference_number():
    with pytest.raises(ValidationError):
        Tender(
            title="Road Construction",
            reference_number="   ",
            deadline="2026-11-15",
        )
