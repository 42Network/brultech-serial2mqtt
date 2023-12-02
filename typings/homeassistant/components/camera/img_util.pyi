"""
This type stub file was generated by pyright.
"""

from typing import Literal, TYPE_CHECKING
from turbojpeg import TurboJPEG
from . import Image

"""Image processing for cameras."""
SUPPORTED_SCALING_FACTORS = ...
_LOGGER = ...
JPEG_QUALITY = ...
if TYPE_CHECKING:
    ...
def find_supported_scaling_factor(current_width: int, current_height: int, target_width: int, target_height: int) -> tuple[int, int] | None:
    """Find a supported scaling factor to scale the image.

    If there is no exact match, we use one size up to ensure
    the image remains crisp.
    """
    ...

def scale_jpeg_camera_image(cam_image: Image, width: int, height: int) -> bytes:
    """Scale a camera image.

    Scale as close as possible to one of the supported scaling factors.
    """
    ...

class TurboJPEGSingleton:
    """Load TurboJPEG only once.

    Ensures we do not log load failures each snapshot
    since camera image fetches happen every few
    seconds.
    """
    __instance: TurboJPEG | Literal[False] | None = ...
    @staticmethod
    def instance() -> TurboJPEG | Literal[False] | None:
        """Singleton for TurboJPEG."""
        ...
    
    def __init__(self) -> None:
        """Try to create TurboJPEG only once."""
        ...
    


