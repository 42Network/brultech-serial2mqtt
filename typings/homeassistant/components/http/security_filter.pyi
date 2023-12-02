"""
This type stub file was generated by pyright.
"""

from typing import Final
from aiohttp.web import Application
from homeassistant.core import callback

"""Middleware to add some basic security filtering to requests."""
_LOGGER = ...
FILTERS: Final = ...
UNSAFE_URL_BYTES = ...
@callback
def setup_security_filter(app: Application) -> None:
    """Create security filter middleware for the app."""
    ...

