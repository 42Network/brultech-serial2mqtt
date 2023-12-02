"""
This type stub file was generated by pyright.
"""

import voluptuous as vol
from typing import Any
from homeassistant.components import websocket_api
from homeassistant.components.websocket_api.connection import ActiveConnection
from homeassistant.core import HomeAssistant, callback
from .const import LOGSEVERITY
from .helpers import LogPersistance

"""Websocket API handlers for the logger integration."""
@callback
def async_load_websocket_api(hass: HomeAssistant) -> None:
    """Set up the websocket API."""
    ...

@callback
@websocket_api.websocket_command({ vol.Required("type"): "logger/log_info" })
def handle_integration_log_info(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None:
    """Handle integrations logger info."""
    ...

@websocket_api.websocket_command({ vol.Required("type"): "logger/integration_log_level",vol.Required("integration"): str,vol.Required("level"): vol.In(LOGSEVERITY),vol.Required("persistence"): vol.Coerce(LogPersistance) })
@websocket_api.async_response
async def handle_integration_log_level(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None:
    """Handle setting integration log level."""
    ...

@websocket_api.websocket_command({ vol.Required("type"): "logger/log_level",vol.Required("module"): str,vol.Required("level"): vol.In(LOGSEVERITY),vol.Required("persistence"): vol.Coerce(LogPersistance) })
@websocket_api.async_response
async def handle_module_log_level(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None:
    """Handle setting integration log level."""
    ...

