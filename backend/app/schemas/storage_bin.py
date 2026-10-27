from pydantic import BaseModel, Field
from typing import Optional


class StorageBinCreate(BaseModel):
    bin_code: str = Field(max_length=20)
    shelf_label: str = Field(max_length=100)
    section: Optional[str] = Field(default=None, max_length=100)
    department_cat: Optional[str] = Field(default=None, max_length=50)
    row_label: Optional[str] = Field(default=None, max_length=50)
    rack_number: Optional[str] = Field(default=None, max_length=50)
    shelf_level: Optional[str] = Field(default=None, max_length=50)
    floor_area: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = None
    capacity: Optional[int] = Field(default=None, gt=0)


class StorageBinUpdate(BaseModel):
    shelf_label: Optional[str] = Field(default=None, max_length=100)
    section: Optional[str] = Field(default=None, max_length=100)
    department_cat: Optional[str] = Field(default=None, max_length=50)
    row_label: Optional[str] = Field(default=None, max_length=50)
    rack_number: Optional[str] = Field(default=None, max_length=50)
    shelf_level: Optional[str] = Field(default=None, max_length=50)
    floor_area: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = None
    capacity: Optional[int] = Field(default=None, gt=0)
