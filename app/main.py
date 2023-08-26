from enum import Enum
from fastapi import FastAPI

from app.api import api

app = FastAPI()

@app.get("/")
async def root():
	return api.return_message()