"""
This type stub file was generated by pyright.
"""

import asyncio
import logging
from collections.abc import Awaitable, Callable, Coroutine
from dataclasses import dataclass
from enum import Enum
from typing import Any, Concatenate, TypeVar
from homeassistant.core import HomeAssistant, callback
from homeassistant.exceptions import HomeAssistantError

"""Provide add-on management."""
_AddonManagerT = TypeVar("_AddonManagerT", bound="AddonManager")
_R = TypeVar("_R")
_P = ...
_FuncType = Callable[Concatenate[_AddonManagerT, _P], Awaitable[_R]]
_ReturnFuncType = Callable[Concatenate[_AddonManagerT, _P], Coroutine[Any, Any, _R]]
def api_error(error_message: str) -> Callable[[_FuncType[_AddonManagerT, _P, _R]], _ReturnFuncType[_AddonManagerT, _P, _R]]:
    """Handle HassioAPIError and raise a specific AddonError."""
    ...

@dataclass
class AddonInfo:
    """Represent the current add-on info state."""
    available: bool
    hostname: str | None
    options: dict[str, Any]
    state: AddonState
    update_available: bool
    version: str | None
    ...


class AddonState(Enum):
    """Represent the current state of the add-on."""
    NOT_INSTALLED = ...
    INSTALLING = ...
    UPDATING = ...
    NOT_RUNNING = ...
    RUNNING = ...


class AddonManager:
    """Manage the add-on.

    Methods may raise AddonError.
    Only one instance of this class may exist per add-on
    to keep track of running add-on tasks.
    """
    def __init__(self, hass: HomeAssistant, logger: logging.Logger, addon_name: str, addon_slug: str) -> None:
        """Set up the add-on manager."""
        ...
    
    def task_in_progress(self) -> bool:
        """Return True if any of the add-on tasks are in progress."""
        ...
    
    @api_error("Failed to get the {addon_name} add-on discovery info")
    async def async_get_addon_discovery_info(self) -> dict:
        """Return add-on discovery info."""
        ...
    
    @api_error("Failed to get the {addon_name} add-on info")
    async def async_get_addon_info(self) -> AddonInfo:
        """Return and cache manager add-on info."""
        ...
    
    @callback
    def async_get_addon_state(self, addon_info: dict[str, Any]) -> AddonState:
        """Return the current state of the managed add-on."""
        ...
    
    @api_error("Failed to set the {addon_name} add-on options")
    async def async_set_addon_options(self, config: dict) -> None:
        """Set manager add-on options."""
        ...
    
    @api_error("Failed to install the {addon_name} add-on")
    async def async_install_addon(self) -> None:
        """Install the managed add-on."""
        ...
    
    @api_error("Failed to uninstall the {addon_name} add-on")
    async def async_uninstall_addon(self) -> None:
        """Uninstall the managed add-on."""
        ...
    
    @api_error("Failed to update the {addon_name} add-on")
    async def async_update_addon(self) -> None:
        """Update the managed add-on if needed."""
        ...
    
    @api_error("Failed to start the {addon_name} add-on")
    async def async_start_addon(self) -> None:
        """Start the managed add-on."""
        ...
    
    @api_error("Failed to restart the {addon_name} add-on")
    async def async_restart_addon(self) -> None:
        """Restart the managed add-on."""
        ...
    
    @api_error("Failed to stop the {addon_name} add-on")
    async def async_stop_addon(self) -> None:
        """Stop the managed add-on."""
        ...
    
    @api_error("Failed to create a backup of the {addon_name} add-on")
    async def async_create_backup(self) -> None:
        """Create a partial backup of the managed add-on."""
        ...
    
    async def async_configure_addon(self, addon_config: dict[str, Any]) -> None:
        """Configure the manager add-on, if needed."""
        ...
    
    @callback
    def async_schedule_install_addon(self, catch_error: bool = ...) -> asyncio.Task:
        """Schedule a task that installs the managed add-on.

        Only schedule a new install task if the there's no running task.
        """
        ...
    
    @callback
    def async_schedule_install_setup_addon(self, addon_config: dict[str, Any], catch_error: bool = ...) -> asyncio.Task:
        """Schedule a task that installs and sets up the managed add-on.

        Only schedule a new install task if the there's no running task.
        """
        ...
    
    @callback
    def async_schedule_update_addon(self, catch_error: bool = ...) -> asyncio.Task:
        """Schedule a task that updates and sets up the managed add-on.

        Only schedule a new update task if the there's no running task.
        """
        ...
    
    @callback
    def async_schedule_start_addon(self, catch_error: bool = ...) -> asyncio.Task:
        """Schedule a task that starts the managed add-on.

        Only schedule a new start task if the there's no running task.
        """
        ...
    
    @callback
    def async_schedule_restart_addon(self, catch_error: bool = ...) -> asyncio.Task:
        """Schedule a task that restarts the managed add-on.

        Only schedule a new restart task if the there's no running task.
        """
        ...
    
    @callback
    def async_schedule_setup_addon(self, addon_config: dict[str, Any], catch_error: bool = ...) -> asyncio.Task:
        """Schedule a task that configures and starts the managed add-on.

        Only schedule a new setup task if there's no running task.
        """
        ...
    


class AddonError(HomeAssistantError):
    """Represent an error with the managed add-on."""
    ...


