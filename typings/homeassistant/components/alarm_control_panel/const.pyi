"""
This type stub file was generated by pyright.
"""

from enum import IntFlag, StrEnum
from typing import Final

"""Provides the constants needed for component."""
DOMAIN: Final = ...
ATTR_CHANGED_BY: Final = ...
ATTR_CODE_ARM_REQUIRED: Final = ...
class CodeFormat(StrEnum):
    """Code formats for the Alarm Control Panel."""
    TEXT = ...
    NUMBER = ...


FORMAT_TEXT: Final = ...
FORMAT_NUMBER: Final = ...
class AlarmControlPanelEntityFeature(IntFlag):
    """Supported features of the alarm control panel entity."""
    ARM_HOME = ...
    ARM_AWAY = ...
    ARM_NIGHT = ...
    TRIGGER = ...
    ARM_CUSTOM_BYPASS = ...
    ARM_VACATION = ...


SUPPORT_ALARM_ARM_HOME: Final = ...
SUPPORT_ALARM_ARM_AWAY: Final = ...
SUPPORT_ALARM_ARM_NIGHT: Final = ...
SUPPORT_ALARM_TRIGGER: Final = ...
SUPPORT_ALARM_ARM_CUSTOM_BYPASS: Final = ...
SUPPORT_ALARM_ARM_VACATION: Final = ...
CONDITION_TRIGGERED: Final = ...
CONDITION_DISARMED: Final = ...
CONDITION_ARMED_HOME: Final = ...
CONDITION_ARMED_AWAY: Final = ...
CONDITION_ARMED_NIGHT: Final = ...
CONDITION_ARMED_VACATION: Final = ...
CONDITION_ARMED_CUSTOM_BYPASS: Final = ...
