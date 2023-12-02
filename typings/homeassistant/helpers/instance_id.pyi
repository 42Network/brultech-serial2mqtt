"""
This type stub file was generated by pyright.
"""

from homeassistant.core import HomeAssistant
from . import singleton

"""Helper to create a unique instance ID."""
DATA_KEY = ...
DATA_VERSION = ...
LEGACY_UUID_FILE = ...
_LOGGER = ...
@singleton.singleton(DATA_KEY)
async def async_get(hass: HomeAssistant) -> str:
    """Get unique ID for the hass instance."""
    ...

