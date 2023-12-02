"""
This type stub file was generated by pyright.
"""

import yaml
from io import StringIO
from pathlib import Path
from typing import Any, TextIO, TypeVar

"""Custom loader."""
JSON_TYPE = list | dict | str
_DictT = TypeVar("_DictT", bound=dict)
_LOGGER = ...
class Secrets:
    """Store secrets while loading YAML."""
    def __init__(self, config_dir: Path) -> None:
        """Initialize secrets."""
        ...
    
    def get(self, requester_path: str, secret: str) -> str:
        """Return the value of a secret."""
        ...
    


class _LoaderMixin:
    """Mixin class with extensions for YAML loader."""
    name: str
    stream: Any
    def get_name(self) -> str:
        """Get the name of the loader."""
        ...
    
    def get_stream_name(self) -> str:
        """Get the name of the stream."""
        ...
    


class FastSafeLoader(FastestAvailableSafeLoader, _LoaderMixin):
    """The fastest available safe loader, either C or Python."""
    def __init__(self, stream: Any, secrets: Secrets | None = ...) -> None:
        """Initialize a safe line loader."""
        ...
    


class SafeLoader(FastSafeLoader):
    """Provided for backwards compatibility. Logs when instantiated."""
    def __init__(*args: Any, **kwargs: Any) -> None:
        """Log a warning and call super."""
        ...
    


class PythonSafeLoader(yaml.SafeLoader, _LoaderMixin):
    """Python safe loader."""
    def __init__(self, stream: Any, secrets: Secrets | None = ...) -> None:
        """Initialize a safe line loader."""
        ...
    


class SafeLineLoader(PythonSafeLoader):
    """Provided for backwards compatibility. Logs when instantiated."""
    def __init__(*args: Any, **kwargs: Any) -> None:
        """Log a warning and call super."""
        ...
    


LoaderType = FastSafeLoader | PythonSafeLoader
def load_yaml(fname: str, secrets: Secrets | None = ...) -> JSON_TYPE:
    """Load a YAML file."""
    ...

def parse_yaml(content: str | TextIO | StringIO, secrets: Secrets | None = ...) -> JSON_TYPE:
    """Parse YAML with the fastest available loader."""
    ...

def secret_yaml(loader: LoaderType, node: yaml.nodes.Node) -> JSON_TYPE:
    """Load secrets and embed it into the configuration YAML."""
    ...

def add_constructor(tag: Any, constructor: Any) -> None:
    """Add to constructor to all loaders."""
    ...

