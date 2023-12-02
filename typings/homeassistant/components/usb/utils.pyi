"""
This type stub file was generated by pyright.
"""

from serial.tools.list_ports_common import ListPortInfo
from .models import USBDevice

"""The USB Discovery integration."""
def usb_device_from_port(port: ListPortInfo) -> USBDevice:
    """Convert serial ListPortInfo to USBDevice."""
    ...

