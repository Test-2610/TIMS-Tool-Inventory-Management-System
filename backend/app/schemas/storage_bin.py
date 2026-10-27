from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, Optional


class StorageBinCreate(BaseModel):
    bin_code: str
    shelf_label: str
    section: Optional[str] = None
    department_cat: Optional[str] = None
    row_label: Optional[str] = None
    rack_number: Optional[str] = None
    shelf_level: Optional[str] = None
    floor_area: Optional[str] = None
    description: Optional[str] = None
    capacity: Optional[int] = Field(default=None, gt=0)

    @field_validator('*', mode='before')
    @classmethod
    def trim_strings(cls, value: Any) -> Any:
        if isinstance(value, str):
            value = value.strip()
            return value or None
        return value


class StorageBinUpdate(BaseModel):
    model_config = ConfigDict(extra='forbid')

    shelf_label: Optional[str] = None
    section: Optional[str] = None
    department_cat: Optional[str] = None
    row_label: Optional[str] = None
    rack_number: Optional[str] = None
    shelf_level: Optional[str] = None
    floor_area: Optional[str] = None
    description: Optional[str] = None
    capacity: Optional[int] = Field(default=None, gt=0)

    @field_validator('*', mode='before')
    @classmethod
    def trim_strings(cls, value: Any) -> Any:
        if isinstance(value, str):
            value = value.strip()
            return value or None
        return value
