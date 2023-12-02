"""
This type stub file was generated by pyright.
"""

import attr
from collections.abc import Callable
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import CALLBACK_TYPE, HomeAssistant
from homeassistant.helpers.trigger import TriggerActionType, TriggerInfo
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from .discovery import MQTTDiscoveryPayload
from .mixins import MqttDiscoveryDeviceUpdate

"""Provides device automations for MQTT."""
_LOGGER = ...
CONF_AUTOMATION_TYPE = ...
CONF_DISCOVERY_ID = ...
CONF_SUBTYPE = ...
DEFAULT_ENCODING = ...
DEVICE = ...
MQTT_TRIGGER_BASE = ...
TRIGGER_SCHEMA = ...
TRIGGER_DISCOVERY_SCHEMA = ...
LOG_NAME = ...

@attr.s(slots=True)
class TriggerInstance:
    """Attached trigger settings."""

    action: TriggerActionType = ...
    trigger_info: TriggerInfo = ...
    trigger: Trigger = ...
    remove: CALLBACK_TYPE | None = ...
    async def async_attach_trigger(self) -> None:
        """Attach MQTT trigger."""
        ...

@attr.s(slots=True)
class Trigger:
    """Device trigger settings."""

    device_id: str = ...
    discovery_data: DiscoveryInfoType | None = ...
    hass: HomeAssistant = ...
    payload: str | None = ...
    qos: int | None = ...
    subtype: str = ...
    topic: str | None = ...
    type: str = ...
    value_template: str | None = ...
    trigger_instances: list[TriggerInstance] = ...
    async def add_trigger(
        self, action: TriggerActionType, trigger_info: TriggerInfo
    ) -> Callable[[], None]:
        """Add MQTT trigger."""
        ...

    async def update_trigger(self, config: ConfigType) -> None:
        """Update MQTT device trigger."""
        ...

    def detach_trigger(self) -> None:
        """Remove MQTT device trigger."""
        ...

class MqttDeviceTrigger(MqttDiscoveryDeviceUpdate):
    """Setup a MQTT device trigger with auto discovery."""
    def __init__(
        self,
        hass: HomeAssistant,
        config: ConfigType,
        device_id: str,
        discovery_data: DiscoveryInfoType,
        config_entry: ConfigEntry,
    ) -> None:
        """Initialize."""
        ...

    async def async_setup(self) -> None:
        """Initialize the device trigger."""
        ...

    async def async_update(self, discovery_data: MQTTDiscoveryPayload) -> None:
        """Handle MQTT device trigger discovery updates."""
        ...

    async def async_tear_down(self) -> None:
        """Cleanup device trigger."""
        ...

async def async_setup_trigger(
    hass: HomeAssistant,
    config: ConfigType,
    config_entry: ConfigEntry,
    discovery_data: DiscoveryInfoType,
) -> None:
    """Set up the MQTT device trigger."""
    ...

async def async_removed_from_device(hass: HomeAssistant, device_id: str) -> None:
    """Handle Mqtt removed from a device."""
    ...

async def async_get_triggers(
    hass: HomeAssistant, device_id: str
) -> list[dict[str, str]]:
    """List device triggers for MQTT devices."""
    ...

async def async_attach_trigger(
    hass: HomeAssistant,
    config: ConfigType,
    action: TriggerActionType,
    trigger_info: TriggerInfo,
) -> CALLBACK_TYPE:
    """Attach a trigger."""
    ...
