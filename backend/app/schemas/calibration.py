from datetime import date
from typing import Optional

from pydantic import BaseModel, model_validator


class CalibrationRecord(BaseModel):
    calibration_date: date
    service_partner: Optional[str] = None
    notes: Optional[str] = None

    @model_validator(mode="after")
    def reject_future_calibration_date(self) -> "CalibrationRecord":
        if self.calibration_date > date.today():
            raise ValueError("calibration_date cannot be in the future")
        return self
