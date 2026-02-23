from __future__ import annotations

from functools import wraps
from typing import Any, Callable, Optional, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])


def _write_log(message: str, filename: Optional[str]) -> None:
    """Write a log message either to console or to a file."""
    if filename:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(message + "\n")
    else:
        print(message)


def log(func: Optional[F] = None, *, filename: Optional[str] = None) -> Any:
    """
    Decorator for logging function execution.

    If ``filename`` is provided, log messages are appended to that file.
    Otherwise, log messages are printed to console.

    On success:  "<function_name> ok"
    On error:    "<function_name> error: <error_text>. Inputs: (<args>), {<kwargs>}"
    """

    def decorator(inner_func: F) -> F:
        @wraps(inner_func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = inner_func(*args, **kwargs)
                _write_log(f"{inner_func.__name__} ok", filename)
                return result
            except Exception as exc:  # noqa: BLE001
                error_text = str(exc) or exc.__class__.__name__
                _write_log(
                    f"{inner_func.__name__} error: {error_text}. Inputs: {args}, {kwargs}",
                    filename,
                )
                raise

        return cast(F, wrapper)

    # Позволяет использовать и так: @log, и так: @log(filename="...")
    if func is not None:
        return decorator(func)

    return decorator