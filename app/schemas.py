from pydantic import BaseModel
from typing import Optional

# Base Model
class BaseResponse(BaseModel):
    count: int
    next: Optional[str]
    prev: Optional[str]
