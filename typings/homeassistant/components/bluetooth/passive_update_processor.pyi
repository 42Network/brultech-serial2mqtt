"""
This type stub file was generated by pyright.
"""

import dataclasses
import logging
from typing import Any, Generic, TYPE_CHECKING, TypeVar, TypedDict
from homeassistant.core import CALLBACK_TYPE, HomeAssistant, callback
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import Entity, EntityDescription
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from .update_coordinator import BasePassiveBluetoothCoordinator
from collections.abc import Callable
from .models import BluetoothScanningMode, BluetoothServiceInfoBleak

"""Passive update processors for the Bluetooth integration."""
if TYPE_CHECKING:
    ...
STORAGE_KEY = ...
STORAGE_VERSION = ...
STORAGE_SAVE_INTERVAL = ...
PASSIVE_UPDATE_PROCESSOR = ...
_T = TypeVar("_T")
@dataclasses.dataclass(slots=True, frozen=True)
class PassiveBluetoothEntityKey:
    """Key for a passive bluetooth entity.

    Example:
    key: temperature
    device_id: outdoor_sensor_1
    """
    key: str
    device_id: str | None
    def to_string(self) -> str:
        """Convert the key to a string which can be used as JSON key."""
        ...
    
    @classmethod
    def from_string(cls, key: str) -> PassiveBluetoothEntityKey:
        """Convert a string (from JSON) to a key."""
        ...
    


@dataclasses.dataclass(slots=True, frozen=False)
class PassiveBluetoothProcessorData:
    """Data for the passive bluetooth processor."""
    coordinators: set[PassiveBluetoothProcessorCoordinator]
    all_restore_data: dict[str, dict[str, RestoredPassiveBluetoothDataUpdate]]
    ...


class RestoredPassiveBluetoothDataUpdate(TypedDict):
    """Restored PassiveBluetoothDataUpdate."""
    devices: dict[str, DeviceInfo]
    entity_descriptions: dict[str, dict[str, Any]]
    entity_names: dict[str, str | None]
    entity_data: dict[str, Any]
    ...


cached_fields = ...
def deserialize_entity_description(descriptions_class: type[EntityDescription], data: dict[str, Any]) -> EntityDescription:
    """Deserialize an entity description."""
    ...

def serialize_entity_description(description: EntityDescription) -> dict[str, Any]:
    """Serialize an entity description."""
    ...

@dataclasses.dataclass(slots=True, frozen=False)
class PassiveBluetoothDataUpdate(Generic[_T]):
    """Generic bluetooth data."""
    devices: dict[str | None, DeviceInfo] = ...
    entity_descriptions: dict[PassiveBluetoothEntityKey, EntityDescription] = ...
    entity_names: dict[PassiveBluetoothEntityKey, str | None] = ...
    entity_data: dict[PassiveBluetoothEntityKey, _T] = ...
    def update(self, new_data: PassiveBluetoothDataUpdate[_T]) -> set[PassiveBluetoothEntityKey] | None:
        """Update the data and returned changed PassiveBluetoothEntityKey or None on device change.

        The changed PassiveBluetoothEntityKey can be used to filter
        which listeners are called.
        """
        ...
    
    def async_get_restore_data(self) -> RestoredPassiveBluetoothDataUpdate:
        """Serialize restore data to storage."""
        ...
    
    @callback
    def async_set_restore_data(self, restore_data: RestoredPassiveBluetoothDataUpdate, entity_description_class: type[EntityDescription]) -> None:
        """Set the restored data from storage."""
        ...
    


def async_register_coordinator_for_restore(hass: HomeAssistant, coordinator: PassiveBluetoothProcessorCoordinator) -> CALLBACK_TYPE:
    """Register a coordinator to have its processors data restored."""
    ...

async def async_setup(hass: HomeAssistant) -> None:
    """Set up the passive update processor coordinators."""
    ...

class PassiveBluetoothProcessorCoordinator(Generic[_T], BasePassiveBluetoothCoordinator):
    """Passive bluetooth processor coordinator for bluetooth advertisements.

    The coordinator is responsible for dispatching the bluetooth data,
    to each processor, and tracking devices.

    The update_method should return the data that is dispatched to each processor.
    This is normally a parsed form of the data, but you can just forward the
    BluetoothServiceInfoBleak if needed.
    """
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, address: str, mode: BluetoothScanningMode, update_method: Callable[[BluetoothServiceInfoBleak], _T], connectable: bool = ...) -> None:
        """Initialize the coordinator."""
        ...
    
    @property
    def available(self) -> bool:
        """Return if the device is available."""
        ...
    
    @callback
    def async_get_restore_data(self) -> dict[str, RestoredPassiveBluetoothDataUpdate]:
        """Generate the restore data."""
        ...
    
    @callback
    def async_register_processor(self, processor: PassiveBluetoothDataProcessor, entity_description_class: type[EntityDescription] | None = ...) -> Callable[[], None]:
        """Register a processor that subscribes to updates."""
        ...
    


_PassiveBluetoothDataProcessorT = TypeVar("_PassiveBluetoothDataProcessorT", bound="PassiveBluetoothDataProcessor[Any]")
class PassiveBluetoothDataProcessor(Generic[_T]):
    """Passive bluetooth data processor for bluetooth advertisements.

    The processor is responsible for keeping track of the bluetooth data
    and updating subscribers.

    The update_method must return a PassiveBluetoothDataUpdate object. Callers
    are responsible for formatting the data returned from their parser into
    the appropriate format.

    The processor will call the update_method every time the bluetooth device
    receives a new advertisement data from the coordinator with the data
    returned by the update_method of the coordinator.

    As the size of each advertisement is limited, the update_method should
    return a PassiveBluetoothDataUpdate object that contains only data that
    should be updated. The coordinator will then dispatch subscribers based
    on the data in the PassiveBluetoothDataUpdate object. The accumulated data
    is available in the devices, entity_data, and entity_descriptions attributes.
    """
    coordinator: PassiveBluetoothProcessorCoordinator
    data: PassiveBluetoothDataUpdate[_T]
    entity_names: dict[PassiveBluetoothEntityKey, str | None]
    entity_data: dict[PassiveBluetoothEntityKey, _T]
    entity_descriptions: dict[PassiveBluetoothEntityKey, EntityDescription]
    devices: dict[str | None, DeviceInfo]
    restore_key: str | None
    def __init__(self, update_method: Callable[[_T], PassiveBluetoothDataUpdate[_T]], restore_key: str | None = ...) -> None:
        """Initialize the coordinator."""
        ...
    
    @callback
    def async_register_coordinator(self, coordinator: PassiveBluetoothProcessorCoordinator, entity_description_class: type[EntityDescription] | None) -> None:
        """Register a coordinator."""
        ...
    
    @property
    def available(self) -> bool:
        """Return if the device is available."""
        ...
    
    @callback
    def async_handle_unavailable(self) -> None:
        """Handle the device going unavailable."""
        ...
    
    @callback
    def async_add_entities_listener(self, entity_class: type[PassiveBluetoothProcessorEntity], async_add_entities: AddEntitiesCallback) -> Callable[[], None]:
        """Add a listener for new entities."""
        ...
    
    @callback
    def async_add_listener(self, update_callback: Callable[[PassiveBluetoothDataUpdate[_T] | None], None]) -> Callable[[], None]:
        """Listen for all updates."""
        ...
    
    @callback
    def async_add_entity_key_listener(self, update_callback: Callable[[PassiveBluetoothDataUpdate[_T] | None], None], entity_key: PassiveBluetoothEntityKey) -> Callable[[], None]:
        """Listen for updates by device key."""
        ...
    
    @callback
    def async_update_listeners(self, data: PassiveBluetoothDataUpdate[_T] | None, was_available: bool | None = ..., changed_entity_keys: set[PassiveBluetoothEntityKey] | None = ...) -> None:
        """Update all registered listeners."""
        ...
    
    @callback
    def async_handle_update(self, update: _T, was_available: bool | None = ...) -> None:
        """Handle a Bluetooth event."""
        ...
    


class PassiveBluetoothProcessorEntity(Entity, Generic[_PassiveBluetoothDataProcessorT]):
    """A class for entities using PassiveBluetoothDataProcessor."""
    _attr_has_entity_name = ...
    _attr_should_poll = ...
    def __init__(self, processor: _PassiveBluetoothDataProcessorT, entity_key: PassiveBluetoothEntityKey, description: EntityDescription, context: Any = ...) -> None:
        """Create the entity with a PassiveBluetoothDataProcessor."""
        ...
    
    @property
    def available(self) -> bool:
        """Return if entity is available."""
        ...
    
    async def async_added_to_hass(self) -> None:
        """When entity is added to hass."""
        ...
    


