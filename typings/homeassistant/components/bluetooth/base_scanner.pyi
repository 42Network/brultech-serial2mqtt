"""
This type stub file was generated by pyright.
"""

from abc import ABC, abstractmethod
from collections.abc import Callable, Generator
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Final
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
from home_assistant_bluetooth import BluetoothServiceInfoBleak
from homeassistant.core import CALLBACK_TYPE, HomeAssistant, callback as hass_callback
from .models import HaBluetoothConnector

"""Base classes for HA Bluetooth scanners for bluetooth."""
MONOTONIC_TIME: Final = ...
_LOGGER = ...
@dataclass(slots=True)
class BluetoothScannerDevice:
    """Data for a bluetooth device from a given scanner."""
    scanner: BaseHaScanner
    ble_device: BLEDevice
    advertisement: AdvertisementData
    ...


class BaseHaScanner(ABC):
    """Base class for Ha Scanners."""
    __slots__ = ...
    def __init__(self, hass: HomeAssistant, source: str, adapter: str, connector: HaBluetoothConnector | None = ...) -> None:
        """Initialize the scanner."""
        ...
    
    @contextmanager
    def connecting(self) -> Generator[None, None, None]:
        """Context manager to track connecting state."""
        ...
    
    @property
    @abstractmethod
    def discovered_devices(self) -> list[BLEDevice]:
        """Return a list of discovered devices."""
        ...
    
    @property
    @abstractmethod
    def discovered_devices_and_advertisement_data(self) -> dict[str, tuple[BLEDevice, AdvertisementData]]:
        """Return a list of discovered devices and their advertisement data."""
        ...
    
    async def async_diagnostics(self) -> dict[str, Any]:
        """Return diagnostic information about the scanner."""
        ...
    


class BaseHaRemoteScanner(BaseHaScanner):
    """Base class for a Home Assistant remote BLE scanner."""
    __slots__ = ...
    def __init__(self, hass: HomeAssistant, scanner_id: str, name: str, new_info_callback: Callable[[BluetoothServiceInfoBleak], None], connector: HaBluetoothConnector | None, connectable: bool) -> None:
        """Initialize the scanner."""
        ...
    
    @hass_callback
    def async_setup(self) -> CALLBACK_TYPE:
        """Set up the scanner."""
        ...
    
    @property
    def discovered_devices(self) -> list[BLEDevice]:
        """Return a list of discovered devices."""
        ...
    
    @property
    def discovered_devices_and_advertisement_data(self) -> dict[str, tuple[BLEDevice, AdvertisementData]]:
        """Return a list of discovered devices and advertisement data."""
        ...
    
    async def async_diagnostics(self) -> dict[str, Any]:
        """Return diagnostic information about the scanner."""
        ...
    


