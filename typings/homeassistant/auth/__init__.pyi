"""
This type stub file was generated by pyright.
"""

from __future__ import annotations

import asyncio
from collections import OrderedDict
from datetime import timedelta
from typing import Any, Dict, Mapping, Optional, Tuple, cast

import jwt
from homeassistant import data_entry_flow
from homeassistant.core import CALLBACK_TYPE, HomeAssistant, callback
from homeassistant.data_entry_flow import FlowResult
from homeassistant.util import dt as dt_util

from . import auth_store, models
from .const import ACCESS_TOKEN_EXPIRATION, GROUP_ID_ADMIN
from .mfa_modules import MultiFactorAuthModule, auth_mfa_module_from_config
from .providers import AuthProvider, LoginFlow, auth_provider_from_config

"""Provide an authentication layer for Home Assistant."""
EVENT_USER_ADDED = ...
EVENT_USER_REMOVED = ...
_MfaModuleDict = Dict[str, MultiFactorAuthModule]
_ProviderKey = Tuple[str, Optional[str]]
_ProviderDict = Dict[_ProviderKey, AuthProvider]

class InvalidAuthError(Exception):
    """Raised when a authentication error occurs."""

    ...

class InvalidProvider(Exception):
    """Authentication provider not found."""

    ...

async def auth_manager_from_config(
    hass: HomeAssistant,
    provider_configs: list[dict[str, Any]],
    module_configs: list[dict[str, Any]],
) -> AuthManager:
    """Initialize an auth manager from config.

    CORE_CONFIG_SCHEMA will make sure do duplicated auth providers or
    mfa modules exist in configs.
    """
    ...

class AuthManagerFlowManager(data_entry_flow.FlowManager):
    """Manage authentication flows."""

    def __init__(self, hass: HomeAssistant, auth_manager: AuthManager) -> None:
        """Init auth manager flows."""
        ...
    async def async_create_flow(
        self,
        handler_key: Any,
        *,
        context: dict[str, Any] | None = ...,
        data: dict[str, Any] | None = ...
    ) -> data_entry_flow.FlowHandler:
        """Create a login flow."""
        ...
    async def async_finish_flow(
        self, flow: data_entry_flow.FlowHandler, result: FlowResult
    ) -> FlowResult:
        """Return a user as result of login flow."""
        ...

class AuthManager:
    """Manage the authentication for Home Assistant."""

    def __init__(
        self,
        hass: HomeAssistant,
        store: auth_store.AuthStore,
        providers: _ProviderDict,
        mfa_modules: _MfaModuleDict,
    ) -> None:
        """Initialize the auth manager."""
        ...
    @property
    def auth_providers(self) -> list[AuthProvider]:
        """Return a list of available auth providers."""
        ...
    @property
    def auth_mfa_modules(self) -> list[MultiFactorAuthModule]:
        """Return a list of available auth modules."""
        ...
    def get_auth_provider(
        self, provider_type: str, provider_id: str | None
    ) -> AuthProvider | None:
        """Return an auth provider, None if not found."""
        ...
    def get_auth_providers(self, provider_type: str) -> list[AuthProvider]:
        """Return a List of auth provider of one type, Empty if not found."""
        ...
    def get_auth_mfa_module(self, module_id: str) -> MultiFactorAuthModule | None:
        """Return a multi-factor auth module, None if not found."""
        ...
    async def async_get_users(self) -> list[models.User]:
        """Retrieve all users."""
        ...
    async def async_get_user(self, user_id: str) -> models.User | None:
        """Retrieve a user."""
        ...
    async def async_get_owner(self) -> models.User | None:
        """Retrieve the owner."""
        ...
    async def async_get_group(self, group_id: str) -> models.Group | None:
        """Retrieve all groups."""
        ...
    async def async_get_user_by_credentials(
        self, credentials: models.Credentials
    ) -> models.User | None:
        """Get a user by credential, return None if not found."""
        ...
    async def async_create_system_user(
        self, name: str, group_ids: list[str] | None = ...
    ) -> models.User:
        """Create a system user."""
        ...
    async def async_create_user(
        self, name: str, group_ids: list[str] | None = ...
    ) -> models.User:
        """Create a user."""
        ...
    async def async_get_or_create_user(
        self, credentials: models.Credentials
    ) -> models.User:
        """Get or create a user."""
        ...
    async def async_link_user(
        self, user: models.User, credentials: models.Credentials
    ) -> None:
        """Link credentials to an existing user."""
        ...
    async def async_remove_user(self, user: models.User) -> None:
        """Remove a user."""
        ...
    async def async_update_user(
        self,
        user: models.User,
        name: str | None = ...,
        is_active: bool | None = ...,
        group_ids: list[str] | None = ...,
    ) -> None:
        """Update a user."""
        ...
    async def async_activate_user(self, user: models.User) -> None:
        """Activate a user."""
        ...
    async def async_deactivate_user(self, user: models.User) -> None:
        """Deactivate a user."""
        ...
    async def async_remove_credentials(self, credentials: models.Credentials) -> None:
        """Remove credentials."""
        ...
    async def async_enable_user_mfa(
        self, user: models.User, mfa_module_id: str, data: Any
    ) -> None:
        """Enable a multi-factor auth module for user."""
        ...
    async def async_disable_user_mfa(
        self, user: models.User, mfa_module_id: str
    ) -> None:
        """Disable a multi-factor auth module for user."""
        ...
    async def async_get_enabled_mfa(self, user: models.User) -> dict[str, str]:
        """List enabled mfa modules for user."""
        ...
    async def async_create_refresh_token(
        self,
        user: models.User,
        client_id: str | None = ...,
        client_name: str | None = ...,
        client_icon: str | None = ...,
        token_type: str | None = ...,
        access_token_expiration: timedelta = ...,
        credential: models.Credentials | None = ...,
    ) -> models.RefreshToken:
        """Create a new refresh token for a user."""
        ...
    async def async_get_refresh_token(
        self, token_id: str
    ) -> models.RefreshToken | None:
        """Get refresh token by id."""
        ...
    async def async_get_refresh_token_by_token(
        self, token: str
    ) -> models.RefreshToken | None:
        """Get refresh token by token."""
        ...
    async def async_remove_refresh_token(
        self, refresh_token: models.RefreshToken
    ) -> None:
        """Delete a refresh token."""
        ...
    @callback
    def async_register_revoke_token_callback(
        self, refresh_token_id: str, revoke_callback: CALLBACK_TYPE
    ) -> CALLBACK_TYPE:
        """Register a callback to be called when the refresh token id is revoked."""
        ...
    @callback
    def async_create_access_token(
        self, refresh_token: models.RefreshToken, remote_ip: str | None = ...
    ) -> str:
        """Create a new access token."""
        ...
    @callback
    def async_validate_refresh_token(
        self, refresh_token: models.RefreshToken, remote_ip: str | None = ...
    ) -> None:
        """Validate that a refresh token is usable.

        Will raise InvalidAuthError on errors.
        """
        ...
    async def async_validate_access_token(
        self, token: str
    ) -> models.RefreshToken | None:
        """Return refresh token if an access token is valid."""
        ...
