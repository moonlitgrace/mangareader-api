from fastapi import HTTPException
import functools
from collections.abc import Callable
from typing import Any


def return_on_404() -> Callable[..., Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return await func(*args, **kwargs)
            # propagates HTTPException from function
            except HTTPException as http_exception:
                raise http_exception
            # catches all other execptions
            except Exception:
                raise HTTPException(status_code=404, detail="Page not found")

        return wrapper

    return decorator
