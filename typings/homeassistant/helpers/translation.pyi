"""
This type stub file was generated by pyright.
"""

from collections.abc import Iterable
from typing import Any
from homeassistant.core import HomeAssistant, callback
from homeassistant.loader import Integration, bind_hass

"""Translation string lookup helpers."""
_LOGGER = ...
TRANSLATION_LOAD_LOCK = ...
TRANSLATION_FLATTEN_CACHE = ...
LOCALE_EN = ...
def recursive_flatten(prefix: Any, data: dict[str, Any]) -> dict[str, Any]:
    """Return a flattened representation of dict data."""
    ...

@callback
def component_translation_path(component: str, language: str, integration: Integration) -> str | None:
    """Return the translation json file location for a component.

    For component:
     - components/hue/translations/nl.json

    For platform:
     - components/hue/translations/light.nl.json

    If component is just a single file, will return None.
    """
    ...

def load_translations_files(translation_files: dict[str, str]) -> dict[str, dict[str, Any]]:
    """Load and parse translation.json files."""
    ...

class _TranslationCache:
    """Cache for flattened translations."""
    __slots__ = ...
    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the cache."""
        ...
    
    async def async_fetch(self, language: str, category: str, components: set[str]) -> list[dict[str, dict[str, Any]]]:
        """Load resources into the cache."""
        ...
    


@bind_hass
async def async_get_translations(hass: HomeAssistant, language: str, category: str, integrations: Iterable[str] | None = ..., config_flow: bool | None = ...) -> dict[str, Any]:
    """Return all backend translations.

    If integration specified, load it for that one.
    Otherwise default to loaded intgrations combined with config flow
    integrations if config_flow is true.
    """
    ...

