from fastapi import HTTPException
import functools
from collections.abc import Callable
from typing import Any, TypeVar

T = TypeVar("T")


def return_on_error(
    return_type: T,
) -> Callable[[Callable[..., Any]], Callable[..., T]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            try:
                return func(*args, **kwargs)
            except AttributeError:
                return return_type

        return wrapper

    return decorator


def return_on_404():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            # propagates HTTPException from function
            except HTTPException:
                raise
            # catches all other execptions
            except Exception:
                raise HTTPException(status_code=404, detail="Page not found")

        return wrapper

    return decorator
