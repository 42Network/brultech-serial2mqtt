"""
This type stub file was generated by pyright.
"""

import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from __future__ import annotations
from dataclasses import dataclass
from datetime import timedelta
from enum import StrEnum
from typing import Any, final
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_MODE, SERVICE_TOGGLE, SERVICE_TURN_OFF, SERVICE_TURN_ON, STATE_ON
from homeassistant.core import HomeAssistant
from homeassistant.helpers.config_validation import PLATFORM_SCHEMA, PLATFORM_SCHEMA_BASE
from homeassistant.helpers.entity import ToggleEntity, ToggleEntityDescription
from homeassistant.helpers.entity_component import EntityComponent
from homeassistant.helpers.typing import ConfigType
from homeassistant.loader import bind_hass
from .const import ATTR_ACTION, ATTR_AVAILABLE_MODES, ATTR_CURRENT_HUMIDITY, ATTR_HUMIDITY, ATTR_MAX_HUMIDITY, ATTR_MIN_HUMIDITY, DEFAULT_MAX_HUMIDITY, DEFAULT_MIN_HUMIDITY, DEVICE_CLASS_DEHUMIDIFIER, DEVICE_CLASS_HUMIDIFIER, DOMAIN, HumidifierAction, HumidifierEntityFeature, MODE_AUTO, MODE_AWAY, MODE_NORMAL, SERVICE_SET_HUMIDITY, SERVICE_SET_MODE, SUPPORT_MODES

"""Provides functionality to interact with humidifier devices."""
_LOGGER = ...
SCAN_INTERVAL = ...
ENTITY_ID_FORMAT = ...
class HumidifierDeviceClass(StrEnum):
    """Device class for humidifiers."""
    HUMIDIFIER = ...
    DEHUMIDIFIER = ...


DEVICE_CLASSES_SCHEMA = ...
DEVICE_CLASSES = ...
@bind_hass
def is_on(hass, entity_id):
    """Return if the humidifier is on based on the statemachine.

    Async friendly.
    """
    ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up humidifier devices."""
    ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up a config entry."""
    ...

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    ...

@dataclass
class HumidifierEntityDescription(ToggleEntityDescription):
    """A class that describes humidifier entities."""
    device_class: HumidifierDeviceClass | None = ...


class HumidifierEntity(ToggleEntity):
    """Base class for humidifier entities."""
    _entity_component_unrecorded_attributes = ...
    entity_description: HumidifierEntityDescription
    _attr_action: HumidifierAction | None = ...
    _attr_available_modes: list[str] | None
    _attr_current_humidity: int | None = ...
    _attr_device_class: HumidifierDeviceClass | None
    _attr_max_humidity: int = ...
    _attr_min_humidity: int = ...
    _attr_mode: str | None
    _attr_supported_features: HumidifierEntityFeature = ...
    _attr_target_humidity: int | None = ...
    @property
    def capability_attributes(self) -> dict[str, Any]:
        """Return capability attributes."""
        ...
    
    @property
    def device_class(self) -> HumidifierDeviceClass | None:
        """Return the class of this entity."""
        ...
    
    @final
    @property
    def state_attributes(self) -> dict[str, Any]:
        """Return the optional state attributes."""
        ...
    
    @property
    def action(self) -> HumidifierAction | None:
        """Return the current action."""
        ...
    
    @property
    def current_humidity(self) -> int | None:
        """Return the current humidity."""
        ...
    
    @property
    def target_humidity(self) -> int | None:
        """Return the humidity we try to reach."""
        ...
    
    @property
    def mode(self) -> str | None:
        """Return the current mode, e.g., home, auto, baby.

        Requires HumidifierEntityFeature.MODES.
        """
        ...
    
    @property
    def available_modes(self) -> list[str] | None:
        """Return a list of available modes.

        Requires HumidifierEntityFeature.MODES.
        """
        ...
    
    def set_humidity(self, humidity: int) -> None:
        """Set new target humidity."""
        ...
    
    async def async_set_humidity(self, humidity: int) -> None:
        """Set new target humidity."""
        ...
    
    def set_mode(self, mode: str) -> None:
        """Set new mode."""
        ...
    
    async def async_set_mode(self, mode: str) -> None:
        """Set new mode."""
        ...
    
    @property
    def min_humidity(self) -> int:
        """Return the minimum humidity."""
        ...
    
    @property
    def max_humidity(self) -> int:
        """Return the maximum humidity."""
        ...
    
    @property
    def supported_features(self) -> HumidifierEntityFeature:
        """Return the list of supported features."""
        ...
    


