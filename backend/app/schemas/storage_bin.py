from pydantic import BaseModel, Field, field_validator
from typing import Any, Optional


class StorageBinCreate(BaseModel):
    bin_code: str = Field(min_length=1)
    shelf_label: str = Field(min_length=1)
    section: Optional[str] = None
    department_cat: Optional[str] = None
    row_label: Optional[str] = None
    rack_number: Optional[str] = None
    shelf_level: Optional[str] = None
    floor_area: Optional[str] = None
    description: Optional[str] = None
    capacity: Optional[int] = Field(default=None, gt=0)

    @field_validator("bin_code", "shelf_label", mode="before")
    @classmethod
    def trim_required_text(cls, value: Any) -> Any:
        return value.strip() if isinstance(value, str) else value


class StorageBinUpdate(BaseModel):
    shelf_label: Optional[str] = Field(default=None, min_length=1)
    section: Optional[str] = None
    department_cat: Optional[str] = None
    row_label: Optional[str] = None
    rack_number: Optional[str] = None
    shelf_level: Optional[str] = None
    floor_area: Optional[str] = None
    description: Optional[str] = None
    capacity: Optional[int] = Field(default=None, gt=0)

    @field_validator("shelf_label", mode="before")
    @classmethod
    def trim_shelf_label(cls, value: Any) -> Any:
        return value.strip() if isinstance(value, str) else value
