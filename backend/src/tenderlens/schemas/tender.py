from datetime import date

from pydantic import BaseModel, Field


class Tender(BaseModel):
    title: str = Field(min_length=1)
    reference_number: str = Field(min_length=1)
    deadline: date