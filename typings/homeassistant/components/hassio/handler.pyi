"""
This type stub file was generated by pyright.
"""

import asyncio
import aiohttp
from typing import Any
from homeassistant.core import HomeAssistant
from homeassistant.loader import bind_hass

"""Handler for Hass.io."""
_LOGGER = ...
class HassioAPIError(RuntimeError):
    """Return if a API trow a error."""
    ...


def api_data(funct): # -> (*argv: Unknown, **kwargs: Unknown) -> Coroutine[Any, Any, Unknown]:
    """Return data of an api."""
    ...

@bind_hass
async def async_get_addon_info(hass: HomeAssistant, slug: str) -> dict:
    """Return add-on info.

    The add-on must be installed.
    The caller of the function should handle HassioAPIError.
    """
    ...

@api_data
async def async_get_addon_store_info(hass: HomeAssistant, slug: str) -> dict:
    """Return add-on store info.

    The caller of the function should handle HassioAPIError.
    """
    ...

@bind_hass
async def async_update_diagnostics(hass: HomeAssistant, diagnostics: bool) -> dict:
    """Update Supervisor diagnostics toggle.

    The caller of the function should handle HassioAPIError.
    """
    ...

@bind_hass
@api_data
async def async_install_addon(hass: HomeAssistant, slug: str) -> dict:
    """Install add-on.

    The caller of the function should handle HassioAPIError.
    """
    ...

@bind_hass
@api_data
async def async_uninstall_addon(hass: HomeAssistant, slug: str) -> dict:
    """Uninstall add-on.

    The caller of the function should handle HassioAPIError.
    """
    ...

@bind_hass
@api_data
async def async_update_addon(hass: HomeAssistant, slug: str, backup: bool = ...) -> dict:
    """Update add-on.

    The caller of the function should handle HassioAPIError.
    """
    ...

@bind_hass
@api_data
async def async_start_addon(hass: HomeAssistant, slug: str) -> dict:
    """Start add-on.

    The caller of the function should handle HassioAPIError.
    """
    ...

@bind_hass
@api_data
async def async_restart_addon(hass: HomeAssistant, slug: str) -> dict:
    """Restart add-on.

    The caller of the function should handle HassioAPIError.
    """
    ...

@bind_hass
@api_data
async def async_stop_addon(hass: HomeAssistant, slug: str) -> dict:
    """Stop add-on.

    The caller of the function should handle HassioAPIError.
    """
    ...

@bind_hass
@api_data
async def async_set_addon_options(hass: HomeAssistant, slug: str, options: dict) -> dict:
    """Set add-on options.

    The caller of the function should handle HassioAPIError.
    """
    ...

@bind_hass
async def async_get_addon_discovery_info(hass: HomeAssistant, slug: str) -> dict | None:
    """Return discovery data for an add-on."""
    ...

@bind_hass
@api_data
async def async_create_backup(hass: HomeAssistant, payload: dict, partial: bool = ...) -> dict:
    """Create a full or partial backup.

    The caller of the function should handle HassioAPIError.
    """
    ...

@bind_hass
@api_data
async def async_update_os(hass: HomeAssistant, version: str | None = ...) -> dict:
    """Update Home Assistant Operating System.

    The caller of the function should handle HassioAPIError.
    """
    ...

@bind_hass
@api_data
async def async_update_supervisor(hass: HomeAssistant) -> dict:
    """Update Home Assistant Supervisor.

    The caller of the function should handle HassioAPIError.
    """
    ...

@bind_hass
@api_data
async def async_update_core(hass: HomeAssistant, version: str | None = ..., backup: bool = ...) -> dict:
    """Update Home Assistant Core.

    The caller of the function should handle HassioAPIError.
    """
    ...

@bind_hass
@_api_bool
async def async_apply_suggestion(hass: HomeAssistant, suggestion_uuid: str) -> bool:
    """Apply a suggestion from supervisor's resolution center.

    The caller of the function should handle HassioAPIError.
    """
    ...

@api_data
async def async_get_green_settings(hass: HomeAssistant) -> dict[str, bool]:
    """Return settings specific to Home Assistant Green."""
    ...

@api_data
async def async_set_green_settings(hass: HomeAssistant, settings: dict[str, bool]) -> dict:
    """Set settings specific to Home Assistant Green.

    Returns an empty dict.
    """
    ...

@api_data
async def async_get_yellow_settings(hass: HomeAssistant) -> dict[str, bool]:
    """Return settings specific to Home Assistant Yellow."""
    ...

@api_data
async def async_set_yellow_settings(hass: HomeAssistant, settings: dict[str, bool]) -> dict:
    """Set settings specific to Home Assistant Yellow.

    Returns an empty dict.
    """
    ...

@api_data
async def async_reboot_host(hass: HomeAssistant) -> dict:
    """Reboot the host.

    Returns an empty dict.
    """
    ...

class HassIO:
    """Small API wrapper for Hass.io."""
    def __init__(self, loop: asyncio.AbstractEventLoop, websession: aiohttp.ClientSession, ip: str) -> None:
        """Initialize Hass.io API."""
        ...
    
    @_api_bool
    def is_connected(self): # -> Coroutine[Any, Any, str | Any]:
        """Return true if it connected to Hass.io supervisor.

        This method returns a coroutine.
        """
        ...
    
    @api_data
    def get_info(self): # -> Coroutine[Any, Any, str | Any]:
        """Return generic Supervisor information.

        This method returns a coroutine.
        """
        ...
    
    @api_data
    def get_host_info(self): # -> Coroutine[Any, Any, str | Any]:
        """Return data for Host.

        This method returns a coroutine.
        """
        ...
    
    @api_data
    def get_os_info(self): # -> Coroutine[Any, Any, str | Any]:
        """Return data for the OS.

        This method returns a coroutine.
        """
        ...
    
    @api_data
    def get_core_info(self): # -> Coroutine[Any, Any, str | Any]:
        """Return data for Home Asssistant Core.

        This method returns a coroutine.
        """
        ...
    
    @api_data
    def get_supervisor_info(self): # -> Coroutine[Any, Any, str | Any]:
        """Return data for the Supervisor.

        This method returns a coroutine.
        """
        ...
    
    @api_data
    def get_addon_info(self, addon): # -> Coroutine[Any, Any, str | Any]:
        """Return data for a Add-on.

        This method returns a coroutine.
        """
        ...
    
    @api_data
    def get_core_stats(self): # -> Coroutine[Any, Any, str | Any]:
        """Return stats for the core.

        This method returns a coroutine.
        """
        ...
    
    @api_data
    def get_addon_stats(self, addon): # -> Coroutine[Any, Any, str | Any]:
        """Return stats for an Add-on.

        This method returns a coroutine.
        """
        ...
    
    @api_data
    def get_supervisor_stats(self): # -> Coroutine[Any, Any, str | Any]:
        """Return stats for the supervisor.

        This method returns a coroutine.
        """
        ...
    
    def get_addon_changelog(self, addon): # -> Coroutine[Any, Any, str | Any]:
        """Return changelog for an Add-on.

        This method returns a coroutine.
        """
        ...
    
    @api_data
    def get_store(self): # -> Coroutine[Any, Any, str | Any]:
        """Return data from the store.

        This method returns a coroutine.
        """
        ...
    
    @api_data
    def get_ingress_panels(self): # -> Coroutine[Any, Any, str | Any]:
        """Return data for Add-on ingress panels.

        This method returns a coroutine.
        """
        ...
    
    @_api_bool
    def restart_homeassistant(self): # -> Coroutine[Any, Any, str | Any]:
        """Restart Home-Assistant container.

        This method returns a coroutine.
        """
        ...
    
    @_api_bool
    def stop_homeassistant(self): # -> Coroutine[Any, Any, str | Any]:
        """Stop Home-Assistant container.

        This method returns a coroutine.
        """
        ...
    
    @_api_bool
    def refresh_updates(self): # -> Coroutine[Any, Any, str | Any]:
        """Refresh available updates.

        This method returns a coroutine.
        """
        ...
    
    @api_data
    def retrieve_discovery_messages(self): # -> Coroutine[Any, Any, str | Any]:
        """Return all discovery data from Hass.io API.

        This method returns a coroutine.
        """
        ...
    
    @api_data
    def get_discovery_message(self, uuid): # -> Coroutine[Any, Any, str | Any]:
        """Return a single discovery data message.

        This method returns a coroutine.
        """
        ...
    
    @api_data
    def get_resolution_info(self): # -> Coroutine[Any, Any, str | Any]:
        """Return data for Supervisor resolution center.

        This method returns a coroutine.
        """
        ...
    
    @api_data
    def get_suggestions_for_issue(self, issue_id: str) -> dict[str, Any]:
        """Return suggestions for issue from Supervisor resolution center.

        This method returns a coroutine.
        """
        ...
    
    @_api_bool
    async def update_hass_api(self, http_config, refresh_token): # -> str | Any:
        """Update Home Assistant API data on Hass.io."""
        ...
    
    @_api_bool
    def update_hass_timezone(self, timezone): # -> Coroutine[Any, Any, str | Any]:
        """Update Home-Assistant timezone data on Hass.io.

        This method returns a coroutine.
        """
        ...
    
    @_api_bool
    def update_diagnostics(self, diagnostics: bool): # -> Coroutine[Any, Any, str | Any]:
        """Update Supervisor diagnostics setting.

        This method returns a coroutine.
        """
        ...
    
    @_api_bool
    def apply_suggestion(self, suggestion_uuid: str): # -> Coroutine[Any, Any, str | Any]:
        """Apply a suggestion from supervisor's resolution center.

        This method returns a coroutine.
        """
        ...
    
    async def send_command(self, command, method=..., payload=..., timeout=..., return_text=..., *, source=...): # -> str | Any:
        """Send API command to Hass.io.

        This method is a coroutine.
        """
        ...
    


