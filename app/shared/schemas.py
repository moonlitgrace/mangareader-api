from typing import Optional

from pydantic import BaseModel


# Base Model
class BaseResponse(BaseModel):
    count: int
    next: Optional[str]
    prev: Optional[str]
