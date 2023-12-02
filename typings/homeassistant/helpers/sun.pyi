"""
This type stub file was generated by pyright.
"""

import datetime
import astral
import astral.location
from collections.abc import Callable
from typing import TYPE_CHECKING
from homeassistant.core import HomeAssistant, callback
from homeassistant.loader import bind_hass

"""Helpers for sun events."""
if TYPE_CHECKING:
    ...
DATA_LOCATION_CACHE = ...
ELEVATION_AGNOSTIC_EVENTS = ...
_AstralSunEventCallable = Callable[..., datetime.datetime]
@callback
@bind_hass
def get_astral_location(hass: HomeAssistant) -> tuple[astral.location.Location, astral.Elevation]:
    """Get an astral location for the current Home Assistant configuration."""
    ...

@callback
@bind_hass
def get_astral_event_next(hass: HomeAssistant, event: str, utc_point_in_time: datetime.datetime | None = ..., offset: datetime.timedelta | None = ...) -> datetime.datetime:
    """Calculate the next specified solar event."""
    ...

@callback
def get_location_astral_event_next(location: astral.location.Location, elevation: astral.Elevation, event: str, utc_point_in_time: datetime.datetime | None = ..., offset: datetime.timedelta | None = ...) -> datetime.datetime:
    """Calculate the next specified solar event."""
    ...

@callback
@bind_hass
def get_astral_event_date(hass: HomeAssistant, event: str, date: datetime.date | datetime.datetime | None = ...) -> datetime.datetime | None:
    """Calculate the astral event time for the specified date."""
    ...

@callback
@bind_hass
def is_up(hass: HomeAssistant, utc_point_in_time: datetime.datetime | None = ...) -> bool:
    """Calculate if the sun is currently up."""
    ...

