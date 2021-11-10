"""
This type stub file was generated by pyright.
"""

from abc import abstractmethod

from homeassistant.core import callback
from homeassistant.helpers.entity import DeviceInfo, Entity
from homeassistant.helpers.typing import ConfigType

"""MQTT component mixins and helpers."""
_LOGGER = ...
AVAILABILITY_ALL = ...
AVAILABILITY_ANY = ...
AVAILABILITY_LATEST = ...
AVAILABILITY_MODES = ...
CONF_AVAILABILITY_MODE = ...
CONF_AVAILABILITY_TOPIC = ...
CONF_ENABLED_BY_DEFAULT = ...
CONF_PAYLOAD_AVAILABLE = ...
CONF_PAYLOAD_NOT_AVAILABLE = ...
CONF_JSON_ATTRS_TOPIC = ...
CONF_JSON_ATTRS_TEMPLATE = ...
CONF_IDENTIFIERS = ...
CONF_CONNECTIONS = ...
CONF_MANUFACTURER = ...
CONF_MODEL = ...
CONF_SW_VERSION = ...
CONF_VIA_DEVICE = ...
CONF_DEPRECATED_VIA_HUB = ...
CONF_SUGGESTED_AREA = ...
CONF_CONFIGURATION_URL = ...
MQTT_ATTRIBUTES_BLOCKED = ...
MQTT_AVAILABILITY_SINGLE_SCHEMA = ...
MQTT_AVAILABILITY_LIST_SCHEMA = ...
MQTT_AVAILABILITY_SCHEMA = ...

def validate_device_has_at_least_one_identifier(value: ConfigType) -> ConfigType:
    """Validate that a device info entry has at least one identifying value."""
    ...

MQTT_ENTITY_DEVICE_INFO_SCHEMA = ...
MQTT_ENTITY_COMMON_SCHEMA = ...

async def async_setup_entry_helper(hass, domain, async_setup, schema):  # -> None:
    """Set up entity, automation or tag creation dynamically through MQTT discovery."""
    ...

class MqttAttributes(Entity):
    """Mixin used for platforms that support JSON attributes."""

    _attributes_extra_blocked: frozenset[str] = ...
    def __init__(self, config: dict) -> None:
        """Initialize the JSON attributes mixin."""
        ...
    async def async_added_to_hass(self) -> None:
        """Subscribe MQTT events."""
        ...
    async def attributes_discovery_update(self, config: dict):  # -> None:
        """Handle updated discovery message."""
        ...
    async def async_will_remove_from_hass(self):  # -> None:
        """Unsubscribe when removed."""
        ...
    @property
    def extra_state_attributes(self):  # -> dict[Unknown, Unknown] | None:
        """Return the state attributes."""
        ...

class MqttAvailability(Entity):
    """Mixin used for platforms that report availability."""

    def __init__(self, config: dict) -> None:
        """Initialize the availability mixin."""
        ...
    async def async_added_to_hass(self) -> None:
        """Subscribe MQTT events."""
        ...
    async def availability_discovery_update(self, config: dict):  # -> None:
        """Handle updated discovery message."""
        ...
    @callback
    def async_mqtt_connect(self):  # -> None:
        """Update state on connection/disconnection to MQTT broker."""
        ...
    async def async_will_remove_from_hass(self):  # -> None:
        """Unsubscribe when removed."""
        ...
    @property
    def available(self) -> bool:
        """Return if the device is available."""
        ...

async def cleanup_device_registry(hass, device_id):  # -> None:
    """Remove device registry entry if there are no remaining entities or triggers."""
    ...

class MqttDiscoveryUpdate(Entity):
    """Mixin used to handle updated discovery message."""

    def __init__(self, discovery_data, discovery_update=...) -> None:
        """Initialize the discovery update mixin."""
        ...
    async def async_added_to_hass(self) -> None:
        """Subscribe to discovery updates."""
        ...
    async def async_removed_from_registry(self) -> None:
        """Clear retained discovery topic in broker."""
        ...
    @callback
    def add_to_platform_abort(self) -> None:
        """Abort adding an entity to a platform."""
        ...
    async def async_will_remove_from_hass(self) -> None:
        """Stop listening to signal and cleanup discovery data.."""
        ...

def device_info_from_config(config) -> DeviceInfo | None:
    """Return a device description for device registry."""
    ...

class MqttEntityDeviceInfo(Entity):
    """Mixin used for mqtt platforms that support the device registry."""

    def __init__(self, device_config: ConfigType | None, config_entry=...) -> None:
        """Initialize the device mixin."""
        ...
    async def device_info_discovery_update(self, config: dict):  # -> None:
        """Handle updated discovery message."""
        ...
    @property
    def device_info(self) -> DeviceInfo | None:
        """Return a device description for device registry."""
        ...

class MqttEntity(
    MqttAttributes, MqttAvailability, MqttDiscoveryUpdate, MqttEntityDeviceInfo
):
    """Representation of an MQTT entity."""

    def __init__(self, hass, config, config_entry, discovery_data) -> None:
        """Init the MQTT Entity."""
        ...
    async def async_added_to_hass(self):  # -> None:
        """Subscribe mqtt events."""
        ...
    async def discovery_update(self, discovery_payload):  # -> None:
        """Handle updated discovery message."""
        ...
    async def async_will_remove_from_hass(self):  # -> None:
        """Unsubscribe when removed."""
        ...
    @staticmethod
    @abstractmethod
    def config_schema():  # -> None:
        """Return the config schema."""
        ...
    @property
    def entity_registry_enabled_default(self) -> bool:
        """Return if the entity should be enabled when first added to the entity registry."""
        ...
    @property
    def entity_category(self) -> str | None:
        """Return the entity category if any."""
        ...
    @property
    def icon(self):
        """Return icon of the entity if any."""
        ...
    @property
    def name(self):
        """Return the name of the device if any."""
        ...
    @property
    def should_poll(self):  # -> Literal[False]:
        """No polling needed."""
        ...
    @property
    def unique_id(self):
        """Return a unique ID."""
        ...
