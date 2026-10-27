from typing import Any, Literal, Optional

from pydantic import BaseModel, Field, field_validator, model_validator


class DamageAssessment(BaseModel):
    damage_type: Literal["theft", "mishandling", "wear_and_tear"]
    market_rate_at_damage: Optional[float] = Field(default=None, gt=0)
    notes: Optional[str] = None

    @model_validator(mode="after")
    def theft_requires_market_rate(self) -> "DamageAssessment":
        if self.damage_type == "theft" and self.market_rate_at_damage is None:
            raise ValueError("market_rate_at_damage is required when damage_type is 'theft'")
        return self


class WriteOffPayload(BaseModel):
    reason: str = Field(min_length=3)
    quantity: int = Field(default=1, ge=1)

    @field_validator("reason", mode="before")
    @classmethod
    def trim_reason(cls, value: Any) -> Any:
        return value.strip() if isinstance(value, str) else value
