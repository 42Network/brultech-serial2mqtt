"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING
from aiohttp import web
from homeassistant.core import HomeAssistant, callback
from .const import HLS_PROVIDER
from .core import IdleTimer, PROVIDERS, StreamOutput, StreamSettings, StreamView
from homeassistant.components.camera import DynamicStreamSettings
from . import Stream

"""Provide functionality to stream HLS."""
if TYPE_CHECKING:
    ...
@callback
def async_setup_hls(hass: HomeAssistant) -> str:
    """Set up api endpoints."""
    ...

@PROVIDERS.register(HLS_PROVIDER)
class HlsStreamOutput(StreamOutput):
    """Represents HLS Output formats."""
    def __init__(self, hass: HomeAssistant, idle_timer: IdleTimer, stream_settings: StreamSettings, dynamic_stream_settings: DynamicStreamSettings) -> None:
        """Initialize HLS output."""
        ...
    
    @property
    def name(self) -> str:
        """Return provider name."""
        ...
    
    def cleanup(self) -> None:
        """Handle cleanup."""
        ...
    
    @property
    def target_duration(self) -> float:
        """Return the target duration."""
        ...
    
    def discontinuity(self) -> None:
        """Fix incomplete segment at end of deque."""
        ...
    


class HlsMasterPlaylistView(StreamView):
    """Stream view used only for Chromecast compatibility."""
    url = ...
    name = ...
    cors_allowed = ...
    @staticmethod
    def render(track: StreamOutput) -> str:
        """Render M3U8 file."""
        ...
    
    async def handle(self, request: web.Request, stream: Stream, sequence: str, part_num: str) -> web.Response:
        """Return m3u8 playlist."""
        ...
    


class HlsPlaylistView(StreamView):
    """Stream view to serve a M3U8 stream."""
    url = ...
    name = ...
    cors_allowed = ...
    @classmethod
    def render(cls, track: HlsStreamOutput) -> str:
        """Render HLS playlist file."""
        ...
    
    @staticmethod
    def bad_request(blocking: bool, target_duration: float) -> web.Response:
        """Return a HTTP Bad Request response."""
        ...
    
    @staticmethod
    def not_found(blocking: bool, target_duration: float) -> web.Response:
        """Return a HTTP Not Found response."""
        ...
    
    async def handle(self, request: web.Request, stream: Stream, sequence: str, part_num: str) -> web.Response:
        """Return m3u8 playlist."""
        ...
    


class HlsInitView(StreamView):
    """Stream view to serve HLS init.mp4."""
    url = ...
    name = ...
    cors_allowed = ...
    async def handle(self, request: web.Request, stream: Stream, sequence: str, part_num: str) -> web.Response:
        """Return init.mp4."""
        ...
    


class HlsPartView(StreamView):
    """Stream view to serve a HLS fmp4 segment."""
    url = ...
    name = ...
    cors_allowed = ...
    async def handle(self, request: web.Request, stream: Stream, sequence: str, part_num: str) -> web.Response:
        """Handle part."""
        ...
    


class HlsSegmentView(StreamView):
    """Stream view to serve a HLS fmp4 segment."""
    url = ...
    name = ...
    cors_allowed = ...
    async def handle(self, request: web.Request, stream: Stream, sequence: str, part_num: str) -> web.StreamResponse:
        """Handle segments."""
        ...
    


