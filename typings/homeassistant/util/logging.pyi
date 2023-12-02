"""
This type stub file was generated by pyright.
"""

import logging
import logging.handlers
from collections.abc import Callable, Coroutine
from typing import Any, TypeVar, overload
from homeassistant.core import HomeAssistant, callback

"""Logging utilities."""
_T = TypeVar("_T")
class HomeAssistantQueueHandler(logging.handlers.QueueHandler):
    """Process the log in another thread."""
    listener: logging.handlers.QueueListener | None = ...
    def prepare(self, record: logging.LogRecord) -> logging.LogRecord:
        """Prepare a record for queuing.

        This is added as a workaround for https://bugs.python.org/issue46755
        """
        ...
    
    def handle(self, record: logging.LogRecord) -> Any:
        """Conditionally emit the specified logging record.

        Depending on which filters have been added to the handler, push the new
        records onto the backing Queue.

        The default python logger Handler acquires a lock
        in the parent class which we do not need as
        SimpleQueue is already thread safe.

        See https://bugs.python.org/issue24645
        """
        ...
    
    def close(self) -> None:
        """Tidy up any resources used by the handler.

        This adds shutdown of the QueueListener
        """
        ...
    


@callback
def async_activate_log_queue_handler(hass: HomeAssistant) -> None:
    """Migrate the existing log handlers to use the queue.

    This allows us to avoid blocking I/O and formatting messages
    in the event loop as log messages are written in another thread.
    """
    ...

def log_exception(format_err: Callable[..., Any], *args: Any) -> None:
    """Log an exception with additional context."""
    ...

@overload
def catch_log_exception(func: Callable[..., Coroutine[Any, Any, Any]], format_err: Callable[..., Any]) -> Callable[..., Coroutine[Any, Any, None]]:
    ...

@overload
def catch_log_exception(func: Callable[..., Any], format_err: Callable[..., Any]) -> Callable[..., None] | Callable[..., Coroutine[Any, Any, None]]:
    ...

def catch_log_exception(func: Callable[..., Any], format_err: Callable[..., Any]) -> Callable[..., None] | Callable[..., Coroutine[Any, Any, None]]:
    """Decorate a function func to catch and log exceptions.

    If func is a coroutine function, a coroutine function will be returned.
    If func is a callback, a callback will be returned.
    """
    ...

def catch_log_coro_exception(target: Coroutine[Any, Any, _T], format_err: Callable[..., Any], *args: Any) -> Coroutine[Any, Any, _T | None]:
    """Decorate a coroutine to catch and log exceptions."""
    ...

def async_create_catching_coro(target: Coroutine[Any, Any, _T]) -> Coroutine[Any, Any, _T | None]:
    """Wrap a coroutine to catch and log exceptions.

    The exception will be logged together with a stacktrace of where the
    coroutine was wrapped.

    target: target coroutine.
    """
    ...

