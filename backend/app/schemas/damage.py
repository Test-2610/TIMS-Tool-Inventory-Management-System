from typing import Any, Literal, Optional

from pydantic import BaseModel, Field, field_validator, model_validator


class DamageAssessment(BaseModel):
    damage_type: Literal['theft', 'mishandling', 'wear_and_tear']
    market_rate_at_damage: Optional[float] = Field(default=None, gt=0)
    notes: Optional[str] = None

    @field_validator('notes', mode='before')
    @classmethod
    def trim_notes(cls, value: Any) -> Any:
        if isinstance(value, str):
            value = value.strip()
            return value or None
        return value

    @model_validator(mode='after')
    def theft_requires_market_rate(self) -> 'DamageAssessment':
        if self.damage_type == 'theft' and self.market_rate_at_damage is None:
            raise ValueError("market_rate_at_damage is required when damage_type is 'theft'")
        return self


class WriteOffPayload(BaseModel):
    reason: str
    quantity: int = Field(default=1, ge=1)

    @field_validator('reason', mode='before')
    @classmethod
    def trim_reason(cls, value: Any) -> Any:
        if isinstance(value, str):
            value = value.strip()
            if not value:
                raise ValueError('reason cannot be blank')
            return value
        return value
