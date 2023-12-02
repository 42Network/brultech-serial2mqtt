"""
This type stub file was generated by pyright.
"""

from collections.abc import Mapping, MutableMapping
from pathlib import Path
from typing import Final
from aiohttp.web_urldispatcher import StaticResource

"""Static file handling for HTTP component."""
CACHE_TIME: Final = ...
CACHE_HEADER = ...
CACHE_HEADERS: Mapping[str, str] = ...
PATH_CACHE: MutableMapping[tuple[str, Path, bool], tuple[Path | None, str | None]] = ...

class CachingStaticResource(StaticResource):
    """Static Resource handler that will add cache headers."""

    ...
