"""
This type stub file was generated by pyright.
"""

import attr
from typing import TYPE_CHECKING
from homeassistant.helpers import device_registry as dr, entity_registry as er

"""Models for permissions."""
if TYPE_CHECKING:
    ...
@attr.s(slots=True)
class PermissionLookup:
    """Class to hold data for permission lookups."""
    entity_registry: er.EntityRegistry = ...
    device_registry: dr.DeviceRegistry = ...


