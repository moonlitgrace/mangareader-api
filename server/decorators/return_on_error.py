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
            except (AttributeError, IndexError):
                return return_type

        return wrapper

    return decorator

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
