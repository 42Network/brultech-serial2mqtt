"""
This type stub file was generated by pyright.
"""

import dataclasses
import fnmatch
import logging
import os
import sys
import voluptuous as vol
from __future__ import annotations
from collections.abc import Coroutine
from typing import Any, TYPE_CHECKING
from serial.tools.list_ports import comports
from serial.tools.list_ports_common import ListPortInfo
from homeassistant import config_entries
from homeassistant.components import websocket_api
from homeassistant.components.websocket_api.connection import ActiveConnection
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED, EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CALLBACK_TYPE, Event, HomeAssistant, callback as hass_callback
from homeassistant.data_entry_flow import BaseServiceInfo
from homeassistant.helpers import config_validation as cv, discovery_flow, system_info
from homeassistant.helpers.debounce import Debouncer
from homeassistant.helpers.typing import ConfigType
from homeassistant.loader import USBMatcher, async_get_usb
from .const import DOMAIN
from .models import USBDevice
from .utils import usb_device_from_port
from pyudev import Device

"""The USB Discovery integration."""
if TYPE_CHECKING:
    ...
_LOGGER = ...
REQUEST_SCAN_COOLDOWN = ...
__all__ = ["async_is_plugged_in", "async_register_scan_request_callback", "USBCallbackMatcher", "UsbServiceInfo"]
CONFIG_SCHEMA = ...
class USBCallbackMatcher(USBMatcher):
    """Callback matcher for the USB integration."""
    ...


@hass_callback
def async_register_scan_request_callback(hass: HomeAssistant, callback: CALLBACK_TYPE) -> CALLBACK_TYPE:
    """Register to receive a callback when a scan should be initiated."""
    ...

@hass_callback
def async_register_initial_scan_callback(hass: HomeAssistant, callback: CALLBACK_TYPE) -> CALLBACK_TYPE:
    """Register to receive a callback when the initial USB scan is done.

    If the initial scan is already done, the callback is called immediately.
    """
    ...

@hass_callback
def async_is_plugged_in(hass: HomeAssistant, matcher: USBCallbackMatcher) -> bool:
    """Return True is a USB device is present."""
    ...

@dataclasses.dataclass(slots=True)
class UsbServiceInfo(BaseServiceInfo):
    """Prepared info from usb entries."""
    device: str
    vid: str
    pid: str
    serial_number: str | None
    manufacturer: str | None
    description: str | None
    ...


def human_readable_device_name(device: str, serial_number: str | None, manufacturer: str | None, description: str | None, vid: str | None, pid: str | None) -> str:
    """Return a human readable name from USBDevice attributes."""
    ...

def get_serial_by_id(dev_path: str) -> str:
    """Return a /dev/serial/by-id match for given device if available."""
    ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the USB Discovery integration."""
    ...

class USBDiscovery:
    """Manage USB Discovery."""
    def __init__(self, hass: HomeAssistant, usb: list[USBMatcher]) -> None:
        """Init USB Discovery."""
        ...
    
    async def async_setup(self) -> None:
        """Set up USB Discovery."""
        ...
    
    async def async_start(self, event: Event) -> None:
        """Start USB Discovery and run a manual scan."""
        ...
    
    async def async_stop(self, event: Event) -> None:
        """Stop USB Discovery."""
        ...
    
    @hass_callback
    def async_register_scan_request_callback(self, _callback: CALLBACK_TYPE) -> CALLBACK_TYPE:
        """Register a scan request callback."""
        ...
    
    @hass_callback
    def async_register_initial_scan_callback(self, callback: CALLBACK_TYPE) -> CALLBACK_TYPE:
        """Register an initial scan callback."""
        ...
    
    async def async_request_scan(self) -> None:
        """Request a serial scan."""
        ...
    


@websocket_api.require_admin
@websocket_api.websocket_command({ vol.Required("type"): "usb/scan" })
@websocket_api.async_response
async def websocket_usb_scan(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None:
    """Scan for new usb devices."""
    ...

