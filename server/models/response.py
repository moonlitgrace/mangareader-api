from pydantic import BaseModel
from typing import Optional


class BaseResponseModel(BaseModel):
    count: int
    next: Optional[str]
    prev: Optional[str]
