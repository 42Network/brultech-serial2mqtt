"""
This type stub file was generated by pyright.
"""

from collections.abc import Callable
from typing import Any, TYPE_CHECKING
from aiohttp import web
from homeassistant.auth.models import RefreshToken, User
from homeassistant.core import Context, HomeAssistant, callback
from homeassistant.util.json import JsonValueType
from .http import WebSocketAdapter

"""Connection session."""
if TYPE_CHECKING:
    ...
current_connection = ...
MessageHandler = Callable[[HomeAssistant, "ActiveConnection", dict[str, Any]], None]
BinaryHandler = Callable[[HomeAssistant, "ActiveConnection", bytes], None]
class ActiveConnection:
    """Handle an active websocket client connection."""
    __slots__ = ...
    def __init__(self, logger: WebSocketAdapter, hass: HomeAssistant, send_message: Callable[[str | dict[str, Any]], None], user: User, refresh_token: RefreshToken) -> None:
        """Initialize an active connection."""
        ...
    
    def __repr__(self) -> str:
        """Return the representation."""
        ...
    
    def set_supported_features(self, features: dict[str, float]) -> None:
        """Set supported features."""
        ...
    
    def get_description(self, request: web.Request | None) -> str:
        """Return a description of the connection."""
        ...
    
    def context(self, msg: dict[str, Any]) -> Context:
        """Return a context."""
        ...
    
    @callback
    def async_register_binary_handler(self, handler: BinaryHandler) -> tuple[int, Callable[[], None]]:
        """Register a temporary binary handler for this connection.

        Returns a binary handler_id (1 byte) and a callback to unregister the handler.
        """
        ...
    
    @callback
    def send_result(self, msg_id: int, result: Any | None = ...) -> None:
        """Send a result message."""
        ...
    
    @callback
    def send_event(self, msg_id: int, event: Any | None = ...) -> None:
        """Send a event message."""
        ...
    
    @callback
    def send_error(self, msg_id: int, code: str, message: str, translation_key: str | None = ..., translation_domain: str | None = ..., translation_placeholders: dict[str, Any] | None = ...) -> None:
        """Send an error message."""
        ...
    
    @callback
    def async_handle_binary(self, handler_id: int, payload: bytes) -> None:
        """Handle a single incoming binary message."""
        ...
    
    @callback
    def async_handle(self, msg: JsonValueType) -> None:
        """Handle a single incoming message."""
        ...
    
    @callback
    def async_handle_close(self) -> None:
        """Handle closing down connection."""
        ...
    
    @callback
    def async_handle_exception(self, msg: dict[str, Any], err: Exception) -> None:
        """Handle an exception while processing a handler."""
        ...
    


