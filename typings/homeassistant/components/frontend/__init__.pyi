"""
This type stub file was generated by pyright.
"""

import logging
import os
import pathlib
import jinja2
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from __future__ import annotations
from collections.abc import Iterator
from functools import lru_cache
from typing import Any, TypedDict
from aiohttp import hdrs, web, web_urldispatcher
from yarl import URL
from homeassistant.components import onboarding, websocket_api
from homeassistant.components.http.view import HomeAssistantView
from homeassistant.components.websocket_api.connection import ActiveConnection
from homeassistant.config import async_hass_config_yaml
from homeassistant.const import CONF_MODE, CONF_NAME, EVENT_PANELS_UPDATED, EVENT_THEMES_UPDATED
from homeassistant.core import HomeAssistant, ServiceCall, callback
from homeassistant.helpers import service
from homeassistant.helpers.json import json_dumps_sorted
from homeassistant.helpers.storage import Store
from homeassistant.helpers.translation import async_get_translations
from homeassistant.helpers.typing import ConfigType
from homeassistant.loader import async_get_integration, bind_hass
from .storage import async_setup_frontend_storage

"""Handle the frontend for Home Assistant."""
DOMAIN = ...
CONF_THEMES = ...
CONF_THEMES_MODES = ...
CONF_THEMES_LIGHT = ...
CONF_THEMES_DARK = ...
CONF_EXTRA_HTML_URL = ...
CONF_EXTRA_HTML_URL_ES5 = ...
CONF_EXTRA_MODULE_URL = ...
CONF_EXTRA_JS_URL_ES5 = ...
CONF_FRONTEND_REPO = ...
CONF_JS_VERSION = ...
DEFAULT_THEME_COLOR = ...
DATA_PANELS = ...
DATA_JS_VERSION = ...
DATA_EXTRA_MODULE_URL = ...
DATA_EXTRA_JS_URL_ES5 = ...
THEMES_STORAGE_KEY = ...
THEMES_STORAGE_VERSION = ...
THEMES_SAVE_DELAY = ...
DATA_THEMES_STORE = ...
DATA_THEMES = ...
DATA_DEFAULT_THEME = ...
DATA_DEFAULT_DARK_THEME = ...
DEFAULT_THEME = ...
VALUE_NO_THEME = ...
PRIMARY_COLOR = ...
_LOGGER = ...
EXTENDED_THEME_SCHEMA = ...
THEME_SCHEMA = ...
CONFIG_SCHEMA = ...
SERVICE_SET_THEME = ...
SERVICE_RELOAD_THEMES = ...
class Manifest:
    """Manage the manifest.json contents."""
    def __init__(self, data: dict) -> None:
        """Init the manifest manager."""
        ...
    
    def __getitem__(self, key: str) -> Any:
        """Return an item in the manifest."""
        ...
    
    @property
    def json(self) -> str:
        """Return the serialized manifest."""
        ...
    
    def update_key(self, key: str, val: str) -> None:
        """Add a keyval to the manifest.json."""
        ...
    


MANIFEST_JSON = ...
class UrlManager:
    """Manage urls to be used on the frontend.

    This is abstracted into a class because
    some integrations add a remove these directly
    on hass.data
    """
    def __init__(self, urls: list[str]) -> None:
        """Init the url manager."""
        ...
    
    def add(self, url: str) -> None:
        """Add a url to the set."""
        ...
    
    def remove(self, url: str) -> None:
        """Remove a url from the set."""
        ...
    


class Panel:
    """Abstract class for panels."""
    component_name: str
    sidebar_icon: str | None = ...
    sidebar_title: str | None = ...
    frontend_url_path: str | None = ...
    config: dict[str, Any] | None = ...
    require_admin = ...
    config_panel_domain: str | None = ...
    def __init__(self, component_name: str, sidebar_title: str | None, sidebar_icon: str | None, frontend_url_path: str | None, config: dict[str, Any] | None, require_admin: bool, config_panel_domain: str | None) -> None:
        """Initialize a built-in panel."""
        ...
    
    @callback
    def to_response(self) -> PanelRespons:
        """Panel as dictionary."""
        ...
    


@bind_hass
@callback
def async_register_built_in_panel(hass: HomeAssistant, component_name: str, sidebar_title: str | None = ..., sidebar_icon: str | None = ..., frontend_url_path: str | None = ..., config: dict[str, Any] | None = ..., require_admin: bool = ..., *, update: bool = ..., config_panel_domain: str | None = ...) -> None:
    """Register a built-in panel."""
    ...

@bind_hass
@callback
def async_remove_panel(hass: HomeAssistant, frontend_url_path: str) -> None:
    """Remove a built-in panel."""
    ...

def add_extra_js_url(hass: HomeAssistant, url: str, es5: bool = ...) -> None:
    """Register extra js or module url to load."""
    ...

def add_manifest_json_key(key: str, val: Any) -> None:
    """Add a keyval to the manifest.json."""
    ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the serving of the frontend."""
    ...

class IndexView(web_urldispatcher.AbstractResource):
    """Serve the frontend."""
    def __init__(self, repo_path: str | None, hass: HomeAssistant) -> None:
        """Initialize the frontend view."""
        ...
    
    @property
    def canonical(self) -> str:
        """Return resource's canonical path."""
        ...
    
    def url_for(self, **kwargs: str) -> URL:
        """Construct url for resource with additional params."""
        ...
    
    async def resolve(self, request: web.Request) -> tuple[web_urldispatcher.UrlMappingMatchInfo | None, set[str]]:
        """Resolve resource.

        Return (UrlMappingMatchInfo, allowed_methods) pair.
        """
        ...
    
    def add_prefix(self, prefix: str) -> None:
        """Add a prefix to processed URLs.

        Required for subapplications support.
        """
        ...
    
    def get_info(self) -> dict[str, list[str]]:
        """Return a dict with additional info useful for introspection."""
        ...
    
    def raw_match(self, path: str) -> bool:
        """Perform a raw match against path."""
        ...
    
    def get_template(self) -> jinja2.Template:
        """Get template."""
        ...
    
    async def get(self, request: web.Request) -> web.Response:
        """Serve the index page for panel pages."""
        ...
    
    def __len__(self) -> int:
        """Return length of resource."""
        ...
    
    def __iter__(self) -> Iterator[web_urldispatcher.ResourceRoute]:
        """Iterate over routes."""
        ...
    


class ManifestJSONView(HomeAssistantView):
    """View to return a manifest.json."""
    requires_auth = ...
    url = ...
    name = ...
    @callback
    def get(self, request: web.Request) -> web.Response:
        """Return the manifest.json."""
        ...
    


@callback
@websocket_api.websocket_command({ "type": "get_panels" })
def websocket_get_panels(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None:
    """Handle get panels command."""
    ...

@callback
@websocket_api.websocket_command({ "type": "frontend/get_themes" })
def websocket_get_themes(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None:
    """Handle get themes command."""
    ...

@websocket_api.websocket_command({ "type": "frontend/get_translations",vol.Required("language"): str,vol.Required("category"): str,vol.Optional("integration"): vol.All(cv.ensure_list, [str]),vol.Optional("config_flow"): bool })
@websocket_api.async_response
async def websocket_get_translations(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None:
    """Handle get translations command."""
    ...

@websocket_api.websocket_command({ "type": "frontend/get_version" })
@websocket_api.async_response
async def websocket_get_version(hass: HomeAssistant, connection: ActiveConnection, msg: dict[str, Any]) -> None:
    """Handle get version command."""
    ...

class PanelRespons(TypedDict):
    """Represent the panel response type."""
    component_name: str
    icon: str | None
    title: str | None
    config: dict[str, Any] | None
    url_path: str | None
    require_admin: bool
    config_panel_domain: str | None
    ...


