"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass
from typing import Final
from homeassistant.components.stream import Orientation
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import UndefinedType

"""Preference management for camera component."""
STORAGE_KEY: Final = ...
STORAGE_VERSION: Final = ...
@dataclass
class DynamicStreamSettings:
    """Stream settings which are managed and updated by the camera entity."""
    preload_stream: bool = ...
    orientation: Orientation = ...


class CameraPreferences:
    """Handle camera preferences."""
    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize camera prefs."""
        ...
    
    async def async_update(self, entity_id: str, *, preload_stream: bool | UndefinedType = ..., orientation: Orientation | UndefinedType = ...) -> dict[str, bool | Orientation]:
        """Update camera preferences.

        Also update the DynamicStreamSettings if they exist.
        preload_stream is stored in a Store
        orientation is stored in the Entity Registry

        Returns a dict with the preferences on success.
        Raises HomeAssistantError on failure.
        """
        ...
    
    async def get_dynamic_stream_settings(self, entity_id: str) -> DynamicStreamSettings:
        """Get the DynamicStreamSettings for the entity."""
        ...
    


