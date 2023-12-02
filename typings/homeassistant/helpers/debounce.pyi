"""
This type stub file was generated by pyright.
"""

from collections.abc import Callable
from logging import Logger
from typing import Generic, TypeVar
from homeassistant.core import HomeAssistant, callback

"""Debounce helper."""
_R_co = TypeVar("_R_co", covariant=True)
class Debouncer(Generic[_R_co]):
    """Class to rate limit calls to a specific command."""
    def __init__(self, hass: HomeAssistant, logger: Logger, *, cooldown: float, immediate: bool, function: Callable[[], _R_co] | None = ...) -> None:
        """Initialize debounce.

        immediate: indicate if the function needs to be called right away and
                   wait <cooldown> until executing next invocation.
        function: optional and can be instantiated later.
        """
        ...
    
    @property
    def function(self) -> Callable[[], _R_co] | None:
        """Return the function being wrapped by the Debouncer."""
        ...
    
    @function.setter
    def function(self, function: Callable[[], _R_co]) -> None:
        """Update the function being wrapped by the Debouncer."""
        ...
    
    async def async_call(self) -> None:
        """Call the function."""
        ...
    
    async def async_shutdown(self) -> None:
        """Cancel any scheduled call, and prevent new runs."""
        ...
    
    @callback
    def async_cancel(self) -> None:
        """Cancel any scheduled call."""
        ...
    


