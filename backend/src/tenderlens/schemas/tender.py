from datetime import date

from pydantic import BaseModel, Field, field_validator


class Tender(BaseModel):
    title: str = Field(min_length=1)
    reference_number: str = Field(min_length=1)
    deadline: date

    @field_validator("title", "reference_number")
    @classmethod
    def validate_non_empty_string(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Field cannot be empty or whitespace")

        return value
