"""
This type stub file was generated by pyright.
"""

import asyncio
import random
import re
import string
import threading
import slugify as unicode_slug
from __future__ import annotations
from collections.abc import Callable, Coroutine, Iterable, KeysView, Mapping
from datetime import datetime, timedelta
from functools import wraps
from typing import Any, TypeVar
from .dt import as_local, utcnow

"""Helper methods for various modules."""
_T = TypeVar("_T")
_U = TypeVar("_U")
RE_SANITIZE_FILENAME = ...
RE_SANITIZE_PATH = ...
def raise_if_invalid_filename(filename: str) -> None:
    """Check if a filename is valid.

    Raises a ValueError if the filename is invalid.
    """
    ...

def raise_if_invalid_path(path: str) -> None:
    """Check if a path is valid.

    Raises a ValueError if the path is invalid.
    """
    ...

def slugify(text: str | None, *, separator: str = ...) -> str:
    """Slugify a given text."""
    ...

def repr_helper(inp: Any) -> str:
    """Help creating a more readable string representation of objects."""
    ...

def convert(value: _T | None, to_type: Callable[[_T], _U], default: _U | None = ...) -> _U | None:
    """Convert value to to_type, returns default if fails."""
    ...

def ensure_unique_string(preferred_string: str, current_strings: Iterable[str] | KeysView[str]) -> str:
    """Return a string that is not present in current_strings.

    If preferred string exists will append _2, _3, ..
    """
    ...

def get_random_string(length: int = ...) -> str:
    """Return a random string with letters and digits."""
    ...

class Throttle:
    """A class for throttling the execution of tasks.

    This method decorator adds a cooldown to a method to prevent it from being
    called more than 1 time within the timedelta interval `min_time` after it
    returned its result.

    Calling a method a second time during the interval will return None.

    Pass keyword argument `no_throttle=True` to the wrapped method to make
    the call not throttled.

    Decorator takes in an optional second timedelta interval to throttle the
    'no_throttle' calls.

    Adds a datetime attribute `last_call` to the method.
    """
    def __init__(self, min_time: timedelta, limit_no_throttle: timedelta | None = ...) -> None:
        """Initialize the throttle."""
        ...
    
    def __call__(self, method: Callable) -> Callable:
        """Caller for the throttle."""
        ...
    


