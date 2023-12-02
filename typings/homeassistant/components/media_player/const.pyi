"""
This type stub file was generated by pyright.
"""

from enum import IntFlag, StrEnum

"""Provides the constants needed for component."""
CONTENT_AUTH_EXPIRY_TIME = ...
ATTR_APP_ID = ...
ATTR_APP_NAME = ...
ATTR_ENTITY_PICTURE_LOCAL = ...
ATTR_GROUP_MEMBERS = ...
ATTR_INPUT_SOURCE = ...
ATTR_INPUT_SOURCE_LIST = ...
ATTR_MEDIA_ANNOUNCE = ...
ATTR_MEDIA_ALBUM_ARTIST = ...
ATTR_MEDIA_ALBUM_NAME = ...
ATTR_MEDIA_ARTIST = ...
ATTR_MEDIA_CHANNEL = ...
ATTR_MEDIA_CONTENT_ID = ...
ATTR_MEDIA_CONTENT_TYPE = ...
ATTR_MEDIA_DURATION = ...
ATTR_MEDIA_ENQUEUE = ...
ATTR_MEDIA_EXTRA = ...
ATTR_MEDIA_EPISODE = ...
ATTR_MEDIA_PLAYLIST = ...
ATTR_MEDIA_POSITION = ...
ATTR_MEDIA_POSITION_UPDATED_AT = ...
ATTR_MEDIA_REPEAT = ...
ATTR_MEDIA_SEASON = ...
ATTR_MEDIA_SEEK_POSITION = ...
ATTR_MEDIA_SERIES_TITLE = ...
ATTR_MEDIA_SHUFFLE = ...
ATTR_MEDIA_TITLE = ...
ATTR_MEDIA_TRACK = ...
ATTR_MEDIA_VOLUME_LEVEL = ...
ATTR_MEDIA_VOLUME_MUTED = ...
ATTR_SOUND_MODE = ...
ATTR_SOUND_MODE_LIST = ...
DOMAIN = ...
class MediaPlayerState(StrEnum):
    """State of media player entities."""
    OFF = ...
    ON = ...
    IDLE = ...
    PLAYING = ...
    PAUSED = ...
    STANDBY = ...
    BUFFERING = ...


class MediaClass(StrEnum):
    """Media class for media player entities."""
    ALBUM = ...
    APP = ...
    ARTIST = ...
    CHANNEL = ...
    COMPOSER = ...
    CONTRIBUTING_ARTIST = ...
    DIRECTORY = ...
    EPISODE = ...
    GAME = ...
    GENRE = ...
    IMAGE = ...
    MOVIE = ...
    MUSIC = ...
    PLAYLIST = ...
    PODCAST = ...
    SEASON = ...
    TRACK = ...
    TV_SHOW = ...
    URL = ...
    VIDEO = ...


MEDIA_CLASS_ALBUM = ...
MEDIA_CLASS_APP = ...
MEDIA_CLASS_ARTIST = ...
MEDIA_CLASS_CHANNEL = ...
MEDIA_CLASS_COMPOSER = ...
MEDIA_CLASS_CONTRIBUTING_ARTIST = ...
MEDIA_CLASS_DIRECTORY = ...
MEDIA_CLASS_EPISODE = ...
MEDIA_CLASS_GAME = ...
MEDIA_CLASS_GENRE = ...
MEDIA_CLASS_IMAGE = ...
MEDIA_CLASS_MOVIE = ...
MEDIA_CLASS_MUSIC = ...
MEDIA_CLASS_PLAYLIST = ...
MEDIA_CLASS_PODCAST = ...
MEDIA_CLASS_SEASON = ...
MEDIA_CLASS_TRACK = ...
MEDIA_CLASS_TV_SHOW = ...
MEDIA_CLASS_URL = ...
MEDIA_CLASS_VIDEO = ...
class MediaType(StrEnum):
    """Media type for media player entities."""
    ALBUM = ...
    APP = ...
    APPS = ...
    ARTIST = ...
    CHANNEL = ...
    CHANNELS = ...
    COMPOSER = ...
    CONTRIBUTING_ARTIST = ...
    EPISODE = ...
    GAME = ...
    GENRE = ...
    IMAGE = ...
    MOVIE = ...
    MUSIC = ...
    PLAYLIST = ...
    PODCAST = ...
    SEASON = ...
    TRACK = ...
    TVSHOW = ...
    URL = ...
    VIDEO = ...


MEDIA_TYPE_ALBUM = ...
MEDIA_TYPE_APP = ...
MEDIA_TYPE_APPS = ...
MEDIA_TYPE_ARTIST = ...
MEDIA_TYPE_CHANNEL = ...
MEDIA_TYPE_CHANNELS = ...
MEDIA_TYPE_COMPOSER = ...
MEDIA_TYPE_CONTRIBUTING_ARTIST = ...
MEDIA_TYPE_EPISODE = ...
MEDIA_TYPE_GAME = ...
MEDIA_TYPE_GENRE = ...
MEDIA_TYPE_IMAGE = ...
MEDIA_TYPE_MOVIE = ...
MEDIA_TYPE_MUSIC = ...
MEDIA_TYPE_PLAYLIST = ...
MEDIA_TYPE_PODCAST = ...
MEDIA_TYPE_SEASON = ...
MEDIA_TYPE_TRACK = ...
MEDIA_TYPE_TVSHOW = ...
MEDIA_TYPE_URL = ...
MEDIA_TYPE_VIDEO = ...
SERVICE_CLEAR_PLAYLIST = ...
SERVICE_JOIN = ...
SERVICE_PLAY_MEDIA = ...
SERVICE_SELECT_SOUND_MODE = ...
SERVICE_SELECT_SOURCE = ...
SERVICE_UNJOIN = ...
class RepeatMode(StrEnum):
    """Repeat mode for media player entities."""
    ALL = ...
    OFF = ...
    ONE = ...


REPEAT_MODE_ALL = ...
REPEAT_MODE_OFF = ...
REPEAT_MODE_ONE = ...
REPEAT_MODES = ...
class MediaPlayerEntityFeature(IntFlag):
    """Supported features of the media player entity."""
    PAUSE = ...
    SEEK = ...
    VOLUME_SET = ...
    VOLUME_MUTE = ...
    PREVIOUS_TRACK = ...
    NEXT_TRACK = ...
    TURN_ON = ...
    TURN_OFF = ...
    PLAY_MEDIA = ...
    VOLUME_STEP = ...
    SELECT_SOURCE = ...
    STOP = ...
    CLEAR_PLAYLIST = ...
    PLAY = ...
    SHUFFLE_SET = ...
    SELECT_SOUND_MODE = ...
    BROWSE_MEDIA = ...
    REPEAT_SET = ...
    GROUPING = ...
    MEDIA_ANNOUNCE = ...
    MEDIA_ENQUEUE = ...


SUPPORT_PAUSE = ...
SUPPORT_SEEK = ...
SUPPORT_VOLUME_SET = ...
SUPPORT_VOLUME_MUTE = ...
SUPPORT_PREVIOUS_TRACK = ...
SUPPORT_NEXT_TRACK = ...
SUPPORT_TURN_ON = ...
SUPPORT_TURN_OFF = ...
SUPPORT_PLAY_MEDIA = ...
SUPPORT_VOLUME_STEP = ...
SUPPORT_SELECT_SOURCE = ...
SUPPORT_STOP = ...
SUPPORT_CLEAR_PLAYLIST = ...
SUPPORT_PLAY = ...
SUPPORT_SHUFFLE_SET = ...
SUPPORT_SELECT_SOUND_MODE = ...
SUPPORT_BROWSE_MEDIA = ...
SUPPORT_REPEAT_SET = ...
SUPPORT_GROUPING = ...
