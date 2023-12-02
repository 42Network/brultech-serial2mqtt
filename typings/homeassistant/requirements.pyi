"""
This type stub file was generated by pyright.
"""

from collections.abc import Iterable
from typing import Any
from .core import HomeAssistant, callback
from .exceptions import HomeAssistantError
from .loader import Integration

"""Module to handle installing requirements."""
PIP_TIMEOUT = ...
MAX_INSTALL_FAILURES = ...
DATA_REQUIREMENTS_MANAGER = ...
CONSTRAINT_FILE = ...
DISCOVERY_INTEGRATIONS: dict[str, Iterable[str]] = ...
_LOGGER = ...

class RequirementsNotFound(HomeAssistantError):
    """Raised when a component is not found."""
    def __init__(self, domain: str, requirements: list[str]) -> None:
        """Initialize a component not found error."""
        ...

async def async_get_integration_with_requirements(
    hass: HomeAssistant, domain: str
) -> Integration:
    """Get an integration with all requirements installed, including the dependencies.

    This can raise IntegrationNotFound if manifest or integration
    is invalid, RequirementNotFound if there was some type of
    failure to install requirements.
    """
    ...

async def async_process_requirements(
    hass: HomeAssistant, name: str, requirements: list[str]
) -> None:
    """Install the requirements for a component or platform.

    This method is a coroutine. It will raise RequirementsNotFound
    if an requirement can't be satisfied.
    """
    ...

@callback
def async_clear_install_history(hass: HomeAssistant) -> None:
    """Forget the install history."""
    ...

def pip_kwargs(config_dir: str | None) -> dict[str, Any]:
    """Return keyword arguments for PIP install."""
    ...

class RequirementsManager:
    """Manage requirements."""
    def __init__(self, hass: HomeAssistant) -> None:
        """Init the requirements manager."""
        ...

    async def async_get_integration_with_requirements(
        self, domain: str, done: set[str] | None = ...
    ) -> Integration:
        """Get an integration with all requirements installed, including dependencies.

        This can raise IntegrationNotFound if manifest or integration
        is invalid, RequirementNotFound if there was some type of
        failure to install requirements.
        """
        ...

    async def async_process_requirements(
        self, name: str, requirements: list[str]
    ) -> None:
        """Install the requirements for a component or platform.

        This method is a coroutine. It will raise RequirementsNotFound
        if an requirement can't be satisfied.
        """
        ...
