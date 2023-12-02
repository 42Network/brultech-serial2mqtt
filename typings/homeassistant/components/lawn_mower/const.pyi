"""
This type stub file was generated by pyright.
"""

from enum import IntFlag, StrEnum

"""Constants for the lawn mower integration."""
class LawnMowerActivity(StrEnum):
    """Activity state of lawn mower devices."""
    ERROR = ...
    PAUSED = ...
    MOWING = ...
    DOCKED = ...


class LawnMowerEntityFeature(IntFlag):
    """Supported features of the lawn mower entity."""
    START_MOWING = ...
    PAUSE = ...
    DOCK = ...


DOMAIN = ...
SERVICE_START_MOWING = ...
SERVICE_PAUSE = ...
SERVICE_DOCK = ...
