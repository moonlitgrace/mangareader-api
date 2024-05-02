from fastapi import HTTPException
import functools


# Return if error happens
def return_on_error(return_type):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (AttributeError, IndexError):
                return return_type

        return wrapper

    return decorator


# Return if page not found
def return_on_404():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
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
