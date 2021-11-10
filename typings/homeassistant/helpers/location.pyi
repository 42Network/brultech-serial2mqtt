"""
This type stub file was generated by pyright.
"""

from collections.abc import Iterable

from homeassistant.core import HomeAssistant, State

"""Location helpers for Home Assistant."""
_LOGGER = ...

def has_location(state: State) -> bool:
    """Test if state contains a valid location.

    Async friendly.
    """
    ...

def closest(latitude: float, longitude: float, states: Iterable[State]) -> State | None:
    """Return closest state to point.

    Async friendly.
    """
    ...

def find_coordinates(
    hass: HomeAssistant, entity_id: str, recursion_history: list | None = ...
) -> str | None:
    """Find the gps coordinates of the entity in the form of '90.000,180.000'."""
    ...
