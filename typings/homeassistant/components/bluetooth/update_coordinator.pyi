"""
This type stub file was generated by pyright.
"""

import logging
from abc import ABC
from homeassistant.core import CALLBACK_TYPE, HomeAssistant, callback
from .models import BluetoothScanningMode

"""Update coordinator for the Bluetooth integration."""
class BasePassiveBluetoothCoordinator(ABC):
    """Base class for passive bluetooth coordinator for bluetooth advertisements.

    The coordinator is responsible for tracking devices.
    """
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, address: str, mode: BluetoothScanningMode, connectable: bool) -> None:
        """Initialize the coordinator."""
        ...
    
    @callback
    def async_start(self) -> CALLBACK_TYPE:
        """Start the data updater."""
        ...
    
    @property
    def name(self) -> str:
        """Return last known name of the device."""
        ...
    
    @property
    def last_seen(self) -> float:
        """Return the last time the device was seen."""
        ...
    
    @property
    def available(self) -> bool:
        """Return if the device is available."""
        ...
    


