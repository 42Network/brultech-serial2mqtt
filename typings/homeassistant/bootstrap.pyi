"""
This type stub file was generated by pyright.
"""

from typing import Any, TYPE_CHECKING
from . import core
from .helpers.typing import ConfigType
from .runner import RuntimeConfig

"""Provide methods to bootstrap a Home Assistant instance."""
if TYPE_CHECKING:
    ...
_LOGGER = ...
ERROR_LOG_FILENAME = ...
DATA_LOGGING = ...
DATA_REGISTRIES_LOADED = ...
LOG_SLOW_STARTUP_INTERVAL = ...
SLOW_STARTUP_CHECK_INTERVAL = ...
STAGE_1_TIMEOUT = ...
STAGE_2_TIMEOUT = ...
WRAP_UP_TIMEOUT = ...
COOLDOWN_TIME = ...
MAX_LOAD_CONCURRENTLY = ...
DEBUGGER_INTEGRATIONS = ...
CORE_INTEGRATIONS = ...
LOGGING_INTEGRATIONS = ...
FRONTEND_INTEGRATIONS = ...
RECORDER_INTEGRATIONS = ...
DISCOVERY_INTEGRATIONS = ...
STAGE_1_INTEGRATIONS = ...
async def async_setup_hass(runtime_config: RuntimeConfig) -> core.HomeAssistant | None:
    """Set up Home Assistant."""
    ...

def open_hass_ui(hass: core.HomeAssistant) -> None:
    """Open the UI."""
    ...

async def load_registries(hass: core.HomeAssistant) -> None:
    """Load the registries and cache the result of platform.uname().processor."""
    ...

async def async_from_config_dict(config: ConfigType, hass: core.HomeAssistant) -> core.HomeAssistant | None:
    """Try to configure Home Assistant from a configuration dictionary.

    Dynamically loads required components and its dependencies.
    This method is a coroutine.
    """
    ...

@core.callback
def async_enable_logging(hass: core.HomeAssistant, verbose: bool = ..., log_rotate_days: int | None = ..., log_file: str | None = ..., log_no_color: bool = ...) -> None:
    """Set up the logging.

    This method must be run in the event loop.
    """
    ...

async def async_mount_local_lib_path(config_dir: str) -> str:
    """Add local library to Python Path.

    This function is a coroutine.
    """
    ...

async def async_setup_multi_components(hass: core.HomeAssistant, domains: set[str], config: dict[str, Any]) -> None:
    """Set up multiple domains. Log on failure."""
    ...

