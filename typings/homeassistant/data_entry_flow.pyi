"""
This type stub file was generated by pyright.
"""

import abc
import voluptuous as vol
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from enum import StrEnum
from typing import Any, Required, TypedDict
from .core import HomeAssistant, callback
from .exceptions import HomeAssistantError

"""Classes to help gather user submissions."""
_LOGGER = ...

class FlowResultType(StrEnum):
    """Result type for a data entry flow."""

    FORM = ...
    CREATE_ENTRY = ...
    ABORT = ...
    EXTERNAL_STEP = ...
    EXTERNAL_STEP_DONE = ...
    SHOW_PROGRESS = ...
    SHOW_PROGRESS_DONE = ...
    MENU = ...

RESULT_TYPE_FORM = ...
RESULT_TYPE_CREATE_ENTRY = ...
RESULT_TYPE_ABORT = ...
RESULT_TYPE_EXTERNAL_STEP = ...
RESULT_TYPE_EXTERNAL_STEP_DONE = ...
RESULT_TYPE_SHOW_PROGRESS = ...
RESULT_TYPE_SHOW_PROGRESS_DONE = ...
RESULT_TYPE_MENU = ...
EVENT_DATA_ENTRY_FLOW_PROGRESSED = ...

@dataclass(slots=True)
class BaseServiceInfo:
    """Base class for discovery ServiceInfo."""

    ...

class FlowError(HomeAssistantError):
    """Base class for data entry errors."""

    ...

class UnknownHandler(FlowError):
    """Unknown handler specified."""

    ...

class UnknownFlow(FlowError):
    """Unknown flow specified."""

    ...

class UnknownStep(FlowError):
    """Unknown step specified."""

    ...

class AbortFlow(FlowError):
    """Exception to indicate a flow needs to be aborted."""
    def __init__(
        self, reason: str, description_placeholders: Mapping[str, str] | None = ...
    ) -> None:
        """Initialize an abort flow exception."""
        ...

class FlowResult(TypedDict, total=False):
    """Typed result dict."""

    context: dict[str, Any]
    data_schema: vol.Schema | None
    data: Mapping[str, Any]
    description_placeholders: Mapping[str, str | None] | None
    description: str | None
    errors: dict[str, str] | None
    extra: str
    flow_id: Required[str]
    handler: Required[str]
    last_step: bool | None
    menu_options: list[str] | dict[str, str]
    options: Mapping[str, Any]
    preview: str | None
    progress_action: str
    reason: str
    required: bool
    result: Any
    step_id: str
    title: str
    type: FlowResultType
    url: str
    version: int
    ...

class FlowManager(abc.ABC):
    """Manage all the flows that are in progress."""
    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the flow manager."""
        ...

    @abc.abstractmethod
    async def async_create_flow(
        self,
        handler_key: str,
        *,
        context: dict[str, Any] | None = ...,
        data: dict[str, Any] | None = ...,
    ) -> FlowHandler:
        """Create a flow for specified handler.

        Handler key is the domain of the component that we want to set up.
        """
        ...

    @abc.abstractmethod
    async def async_finish_flow(
        self, flow: FlowHandler, result: FlowResult
    ) -> FlowResult:
        """Finish a data entry flow."""
        ...

    async def async_post_init(self, flow: FlowHandler, result: FlowResult) -> None:
        """Entry has finished executing its first step asynchronously."""
        ...

    @callback
    def async_has_matching_flow(
        self, handler: str, match_context: dict[str, Any], data: Any
    ) -> bool:
        """Check if an existing matching flow is in progress.

        A flow with the same handler, context, and data.

        If match_context is passed, only return flows with a context that is a
        superset of match_context.
        """
        ...

    @callback
    def async_get(self, flow_id: str) -> FlowResult:
        """Return a flow in progress as a partial FlowResult."""
        ...

    @callback
    def async_progress(self, include_uninitialized: bool = ...) -> list[FlowResult]:
        """Return the flows in progress as a partial FlowResult."""
        ...

    @callback
    def async_progress_by_handler(
        self,
        handler: str,
        include_uninitialized: bool = ...,
        match_context: dict[str, Any] | None = ...,
    ) -> list[FlowResult]:
        """Return the flows in progress by handler as a partial FlowResult.

        If match_context is specified, only return flows with a context that
        is a superset of match_context.
        """
        ...

    @callback
    def async_progress_by_init_data_type(
        self,
        init_data_type: type,
        matcher: Callable[[Any], bool],
        include_uninitialized: bool = ...,
    ) -> list[FlowResult]:
        """Return flows in progress init matching by data type as a partial FlowResult."""
        ...

    async def async_init(
        self, handler: str, *, context: dict[str, Any] | None = ..., data: Any = ...
    ) -> FlowResult:
        """Start a data entry flow."""
        ...

    async def async_configure(
        self, flow_id: str, user_input: dict | None = ...
    ) -> FlowResult:
        """Continue a data entry flow."""
        ...

    @callback
    def async_abort(self, flow_id: str) -> None:
        """Abort a flow."""
        ...

class FlowHandler:
    """Handle a data entry flow."""

    cur_step: FlowResult | None = ...
    flow_id: str = ...
    hass: HomeAssistant = ...
    handler: str = ...
    context: dict[str, Any] = ...
    init_step = ...
    init_data: Any = ...
    VERSION = ...
    @property
    def source(self) -> str | None:
        """Source that initialized the flow."""
        ...

    @property
    def show_advanced_options(self) -> bool:
        """If we should show advanced options."""
        ...

    def add_suggested_values_to_schema(
        self, data_schema: vol.Schema, suggested_values: Mapping[str, Any] | None
    ) -> vol.Schema:
        """Make a copy of the schema, populated with suggested values.

        For each schema marker matching items in `suggested_values`,
        the `suggested_value` will be set. The existing `suggested_value` will
        be left untouched if there is no matching item.
        """
        ...

    @callback
    def async_show_form(
        self,
        *,
        step_id: str,
        data_schema: vol.Schema | None = ...,
        errors: dict[str, str] | None = ...,
        description_placeholders: Mapping[str, str | None] | None = ...,
        last_step: bool | None = ...,
        preview: str | None = ...,
    ) -> FlowResult:
        """Return the definition of a form to gather user input."""
        ...

    @callback
    def async_create_entry(
        self,
        *,
        title: str | None = ...,
        data: Mapping[str, Any],
        description: str | None = ...,
        description_placeholders: Mapping[str, str] | None = ...,
    ) -> FlowResult:
        """Finish flow."""
        ...

    @callback
    def async_abort(
        self, *, reason: str, description_placeholders: Mapping[str, str] | None = ...
    ) -> FlowResult:
        """Abort the flow."""
        ...

    @callback
    def async_external_step(
        self,
        *,
        step_id: str,
        url: str,
        description_placeholders: Mapping[str, str] | None = ...,
    ) -> FlowResult:
        """Return the definition of an external step for the user to take."""
        ...

    @callback
    def async_external_step_done(self, *, next_step_id: str) -> FlowResult:
        """Return the definition of an external step for the user to take."""
        ...

    @callback
    def async_show_progress(
        self,
        *,
        step_id: str,
        progress_action: str,
        description_placeholders: Mapping[str, str] | None = ...,
    ) -> FlowResult:
        """Show a progress message to the user, without user input allowed."""
        ...

    @callback
    def async_show_progress_done(self, *, next_step_id: str) -> FlowResult:
        """Mark the progress done."""
        ...

    @callback
    def async_show_menu(
        self,
        *,
        step_id: str,
        menu_options: list[str] | dict[str, str],
        description_placeholders: Mapping[str, str] | None = ...,
    ) -> FlowResult:
        """Show a navigation menu to the user.

        Options dict maps step_id => i18n label
        """
        ...

    @callback
    def async_remove(self) -> None:
        """Notification that the flow has been removed."""
        ...

    @staticmethod
    async def async_setup_preview(hass: HomeAssistant) -> None:
        """Set up preview."""
        ...
