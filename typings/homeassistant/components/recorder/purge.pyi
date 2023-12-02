"""
This type stub file was generated by pyright.
"""

from collections.abc import Callable
from datetime import datetime
from typing import TYPE_CHECKING
from .util import retryable_database_job
from . import Recorder

"""Purge old data helper."""
if TYPE_CHECKING:
    ...
_LOGGER = ...
DEFAULT_STATES_BATCHES_PER_PURGE = ...
DEFAULT_EVENTS_BATCHES_PER_PURGE = ...
@retryable_database_job("purge")
def purge_old_data(instance: Recorder, purge_before: datetime, repack: bool, apply_filter: bool = ..., events_batch_size: int = ..., states_batch_size: int = ...) -> bool:
    """Purge events and states older than purge_before.

    Cleans up an timeframe of an hour, based on the oldest record.
    """
    ...

@retryable_database_job("purge_entity_data")
def purge_entity_data(instance: Recorder, entity_filter: Callable[[str], bool], purge_before: datetime) -> bool:
    """Purge states and events of specified entities."""
    ...

