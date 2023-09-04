from functools import wraps
from fastapi import HTTPException

def handle_exceptions(error: str, status_code: int):
	def decorator(func):
		@wraps(func)
		async def wrapper(*args, **kwargs):
			try:
				return await func(*args, **kwargs)
			except Exception as e:
				raise HTTPException(
					detail=error,
					status_code=status_code
				)
		return wrapper
	return decorator