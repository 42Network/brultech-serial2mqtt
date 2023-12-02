"""
This type stub file was generated by pyright.
"""

from dataclasses import dataclass

"""Models helper class for the usb integration."""
@dataclass
class USBDevice:
    """A usb device."""
    device: str
    vid: str
    pid: str
    serial_number: str | None
    manufacturer: str | None
    description: str | None
    ...


