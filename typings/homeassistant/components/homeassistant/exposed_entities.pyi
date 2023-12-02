"""
This type stub file was generated by pyright.
"""

import dataclasses
import voluptuous as vol
from collections.abc import Callable, Mapping
from typing import Any, TypedDict
from homeassistant.components import websocket_api
from homeassistant.core import HomeAssistant, callback

"""Control which entities are exposed to voice assistants."""
KNOWN_ASSISTANTS = ...
STORAGE_KEY = ...
STORAGE_VERSION = ...
SAVE_DELAY = ...
DEFAULT_EXPOSED_DOMAINS = ...
DEFAULT_EXPOSED_BINARY_SENSOR_DEVICE_CLASSES = ...
DEFAULT_EXPOSED_SENSOR_DEVICE_CLASSES = ...
DEFAULT_EXPOSED_ASSISTANT = ...
@dataclasses.dataclass(frozen=True)
class AssistantPreferences:
    """Preferences for an assistant."""
    expose_new: bool
    def to_json(self) -> dict[str, Any]:
        """Return a JSON serializable representation for storage."""
        ...
    


@dataclasses.dataclass(frozen=True)
class ExposedEntity:
    """An exposed entity without a unique_id."""
    assistants: dict[str, dict[str, Any]]
    def to_json(self) -> dict[str, Any]:
        """Return a JSON serializable representation for storage."""
        ...
    


class SerializedExposedEntities(TypedDict):
    """Serialized exposed entities storage storage collection."""
    assistants: dict[str, dict[str, Any]]
    exposed_entities: dict[str, dict[str, Any]]
    ...


class ExposedEntities:
    """Control assistant settings.

    Settings for entities without a unique_id are stored in the store.
    Settings for entities with a unique_id are stored in the entity registry.
    """
    _assistants: dict[str, AssistantPreferences]
    entities: dict[str, ExposedEntity]
    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize."""
        ...
    
    async def async_initialize(self) -> None:
        """Finish initializing."""
        ...
    
    @callback
    def async_listen_entity_updates(self, assistant: str, listener: Callable[[], None]) -> None:
        """Listen for updates to entity expose settings."""
        ...
    
    @callback
    def async_set_assistant_option(self, assistant: str, entity_id: str, key: str, value: Any) -> None:
        """Set an option for an assistant.

        Notify listeners if expose flag was changed.
        """
        ...
    
    @callback
    def async_get_expose_new_entities(self, assistant: str) -> bool:
        """Check if new entities are exposed to an assistant."""
        ...
    
    @callback
    def async_set_expose_new_entities(self, assistant: str, expose_new: bool) -> None:
        """Enable an assistant to expose new entities."""
        ...
    
    @callback
    def async_get_assistant_settings(self, assistant: str) -> dict[str, Mapping[str, Any]]:
        """Get all entity expose settings for an assistant."""
        ...
    
    @callback
    def async_get_entity_settings(self, entity_id: str) -> dict[str, Mapping[str, Any]]:
        """Get assistant expose settings for an entity."""
        ...
    
    @callback
    def async_should_expose(self, assistant: str, entity_id: str) -> bool:
        """Return True if an entity should be exposed to an assistant."""
        ...
    


@callback
@websocket_api.require_admin
@websocket_api.websocket_command({ vol.Required("type"): "homeassistant/expose_entity",vol.Required("assistants"): [vol.In(KNOWN_ASSISTANTS)],vol.Required("entity_ids"): [str],vol.Required("should_expose"): bool })
def ws_expose_entity(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None:
    """Expose an entity to an assistant."""
    ...

@callback
@websocket_api.require_admin
@websocket_api.websocket_command({ vol.Required("type"): "homeassistant/expose_entity/list" })
def ws_list_exposed_entities(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None:
    """Expose an entity to an assistant."""
    ...

@callback
@websocket_api.require_admin
@websocket_api.websocket_command({ vol.Required("type"): "homeassistant/expose_new_entities/get",vol.Required("assistant"): vol.In(KNOWN_ASSISTANTS) })
def ws_expose_new_entities_get(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None:
    """Check if new entities are exposed to an assistant."""
    ...

@callback
@websocket_api.require_admin
@websocket_api.websocket_command({ vol.Required("type"): "homeassistant/expose_new_entities/set",vol.Required("assistant"): vol.In(KNOWN_ASSISTANTS),vol.Required("expose_new"): bool })
def ws_expose_new_entities_set(hass: HomeAssistant, connection: websocket_api.ActiveConnection, msg: dict[str, Any]) -> None:
    """Expose new entities to an assistatant."""
    ...

@callback
def async_listen_entity_updates(hass: HomeAssistant, assistant: str, listener: Callable[[], None]) -> None:
    """Listen for updates to entity expose settings."""
    ...

@callback
def async_get_assistant_settings(hass: HomeAssistant, assistant: str) -> dict[str, Mapping[str, Any]]:
    """Get all entity expose settings for an assistant."""
    ...

@callback
def async_get_entity_settings(hass: HomeAssistant, entity_id: str) -> dict[str, Mapping[str, Any]]:
    """Get assistant expose settings for an entity."""
    ...

@callback
def async_expose_entity(hass: HomeAssistant, assistant: str, entity_id: str, should_expose: bool) -> None:
    """Get assistant expose settings for an entity."""
    ...

@callback
def async_should_expose(hass: HomeAssistant, assistant: str, entity_id: str) -> bool:
    """Return True if an entity should be exposed to an assistant."""
    ...

@callback
def async_set_assistant_option(hass: HomeAssistant, assistant: str, entity_id: str, option: str, value: Any) -> None:
    """Set an option for an assistant.

    Notify listeners if expose flag was changed.
    """
    ...

