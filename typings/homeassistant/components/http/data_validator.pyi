"""
This type stub file was generated by pyright.
"""

import voluptuous as vol
from collections.abc import Awaitable, Callable, Coroutine
from typing import Any, Concatenate, TypeVar
from aiohttp import web
from .view import HomeAssistantView

"""Decorator for view methods to help with data validation."""
_HassViewT = TypeVar("_HassViewT", bound=HomeAssistantView)
_P = ...
_LOGGER = ...
class RequestDataValidator:
    """Decorator that will validate the incoming data.

    Takes in a voluptuous schema and adds 'data' as
    keyword argument to the function call.

    Will return a 400 if no JSON provided or doesn't match schema.
    """
    def __init__(self, schema: vol.Schema, allow_empty: bool = ...) -> None:
        """Initialize the decorator."""
        ...
    
    def __call__(self, method: Callable[Concatenate[_HassViewT, web.Request, dict[str, Any], _P], Awaitable[web.Response],]) -> Callable[Concatenate[_HassViewT, web.Request, _P], Coroutine[Any, Any, web.Response],]:
        """Decorate a function."""
        ...
    


