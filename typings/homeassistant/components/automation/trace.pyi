"""
This type stub file was generated by pyright.
"""

from contextlib import contextmanager
from typing import Any

from homeassistant.components.trace import ActionTrace
from homeassistant.core import Context

"""Trace support for automation."""

class AutomationTrace(ActionTrace):
    """Container for automation trace."""

    _domain = ...
    def __init__(
        self,
        item_id: str,
        config: dict[str, Any],
        blueprint_inputs: dict[str, Any],
        context: Context,
    ) -> None:
        """Container for automation trace."""
        ...
    def set_trigger_description(self, trigger: str) -> None:
        """Set trigger description."""
        ...
    def as_short_dict(self) -> dict[str, Any]:
        """Return a brief dictionary version of this AutomationTrace."""
        ...

@contextmanager
def trace_automation(
    hass, automation_id, config, blueprint_inputs, context, trace_config
):  # -> Generator[AutomationTrace, None, None]:
    """Trace action execution of automation with automation_id."""
    ...
