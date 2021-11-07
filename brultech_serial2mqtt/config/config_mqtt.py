from typing import Any, Dict, Optional

from voluptuous import All
from voluptuous import Any as AnyValid
from voluptuous import Optional as OptionalField
from voluptuous import Range
from voluptuous import Required as RequiredField
from voluptuous import Schema

from brultech_serial2mqtt.config.typing import EmptyConfigDict

SCHEMA = Schema(
    {
        OptionalField("birth_message", default=EmptyConfigDict): {
            OptionalField("payload", default="online"): str,
            OptionalField("qos", default=0): All(
                int,
                Range(min=0, max=2),
            ),
            OptionalField("retain", default=False): bool,
            OptionalField("topic", default="brultech-serial2mqtt/status"): str,
        },
        RequiredField("broker"): str,
        OptionalField("client_id", default="brultech-serial2mqtt"): AnyValid(str, None),
        OptionalField("home_assistant", default=EmptyConfigDict): {
            OptionalField("enable", default=True): bool,
            OptionalField("discovery_prefix", default="homeassistant"): str,
            OptionalField("birth_message", default=EmptyConfigDict): {
                OptionalField("topic", default="homeassistant/status"): str,
                OptionalField("payload", default="online"): str,
                OptionalField("qos", default=0): All(
                    int,
                    Range(min=0, max=2),
                ),
            },
        },
        OptionalField("password", default=None): AnyValid(str, None),
        OptionalField("port", default=1883): int,
        OptionalField("topic_prefix", default="brultech-serial2mqtt"): AnyValid(
            str, None
        ),
        OptionalField("username", default=None): AnyValid(str, None),
        OptionalField("will_message", default=EmptyConfigDict): {
            OptionalField("payload", default="offline"): str,
            OptionalField("qos", default=0): All(
                int,
                Range(min=0, max=2),
            ),
            OptionalField("retain", default=False): bool,
            OptionalField("topic", default="brultech-serial2mqtt/status"): str,
        },
    },
)


class BirthWillConfigMixin:
    def __init__(self, birth_will_config: Dict[str, Any]):
        self._topic: str = birth_will_config["topic"]
        self._payload: str = birth_will_config["payload"]
        self._qos: int = birth_will_config["qos"]

    @property
    def topic(self) -> str:
        return self._topic

    @property
    def payload(self) -> str:
        return self._payload

    @property
    def qos(self) -> int:
        return self._qos


class HomeAssistantBirthMessage(BirthWillConfigMixin):
    """Home Assistant birth message config."""


class HomeAssistant:
    """Home Assistant integration config."""

    def __init__(self, home_assistant_config: Dict[str, Any]):
        self._birth_message = HomeAssistantBirthMessage(
            home_assistant_config["birth_message"]
        )
        self._enable = home_assistant_config["enable"]
        self._discovery_prefix = home_assistant_config["discovery_prefix"]

    @property
    def birth_message(self) -> HomeAssistantBirthMessage:
        return self._birth_message

    @property
    def enable(self) -> bool:
        """Return if integration is enabled."""
        return self._enable

    @property
    def discovery_prefix(self) -> str:
        """Return Home Assistant discovery prefix."""
        return self._discovery_prefix


class MQTTBirthWillMessageConfig(BirthWillConfigMixin):
    """MQTT birth/will message sending configuration."""

    def __init__(self, birth_will_config: Dict[str, Any]):
        super().__init__(birth_will_config)
        self._retain: bool = birth_will_config["retain"]

    @property
    def retain(self) -> bool:
        return self._retain


class MQTTConfig:
    """MQTT config."""

    schema = SCHEMA

    def __init__(self, mqtt_config: Dict[str, Any]):
        self._birth_message = MQTTBirthWillMessageConfig(mqtt_config["birth_message"])
        self._broker = mqtt_config["broker"]
        self._client_id = mqtt_config["client_id"]
        self._home_assistant = HomeAssistant(mqtt_config["home_assistant"])
        self._password = mqtt_config["password"]
        self._port = mqtt_config["port"]
        self._topic_prefix = mqtt_config["topic_prefix"]
        self._username = mqtt_config["username"]
        self._will_message = MQTTBirthWillMessageConfig(mqtt_config["will_message"])

    @property
    def birth_message(self) -> MQTTBirthWillMessageConfig:
        return self._birth_message

    @property
    def broker(self) -> str:
        """Return broker IP or hostname."""
        return self._broker

    @property
    def client_id(self) -> Optional[str]:
        """Return client id."""
        return self._client_id

    @property
    def home_assistant(self) -> HomeAssistant:
        """Return Home Assistant integration config."""
        return self._home_assistant

    @property
    def password(self) -> Optional[str]:
        """Return broker password."""
        return self._password

    @property
    def port(self) -> int:
        """Return broker port."""
        return self._port

    @property
    def topic_prefix(self) -> str:
        """Return topic prefix to use when sending to broker."""
        return self._topic_prefix

    @property
    def username(self) -> Optional[str]:
        """Return broker username."""
        return self._username

    @property
    def will_message(self) -> MQTTBirthWillMessageConfig:
        return self._will_message
