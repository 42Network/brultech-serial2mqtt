"""
This type stub file was generated by pyright.
"""

import av
from collections.abc import Callable, Generator, Iterator, Mapping
from io import BytesIO
from threading import Event
from typing import Any, Self
from homeassistant.core import HomeAssistant
from .core import KeyFrameConverter, StreamOutput, StreamSettings
from .diagnostics import Diagnostics

"""Provides the worker thread needed for processing streams."""
_LOGGER = ...
NEGATIVE_INF = ...
class StreamWorkerError(Exception):
    """An exception thrown while processing a stream."""
    ...


class StreamEndedError(StreamWorkerError):
    """Raised when the stream is complete, exposed for facilitating testing."""
    ...


class StreamState:
    """Responsible for trakcing output and playback state for a stream.

    Holds state used for playback to interpret a decoded stream. A source stream
    may be reset (e.g. reconnecting to an rtsp stream) and this object tracks
    the state to inform the player.
    """
    def __init__(self, hass: HomeAssistant, outputs_callback: Callable[[], Mapping[str, StreamOutput]], diagnostics: Diagnostics) -> None:
        """Initialize StreamState."""
        ...
    
    @property
    def sequence(self) -> int:
        """Return the current sequence for the latest segment."""
        ...
    
    def next_sequence(self) -> int:
        """Increment the sequence number."""
        ...
    
    @property
    def stream_id(self) -> int:
        """Return the readonly stream_id attribute."""
        ...
    
    def discontinuity(self) -> None:
        """Mark the stream as having been restarted."""
        ...
    
    @property
    def outputs(self) -> list[StreamOutput]:
        """Return the active stream outputs."""
        ...
    
    @property
    def diagnostics(self) -> Diagnostics:
        """Return diagnostics object."""
        ...
    


class StreamMuxer:
    """StreamMuxer re-packages video/audio packets for output."""
    def __init__(self, hass: HomeAssistant, video_stream: av.video.VideoStream, audio_stream: av.audio.stream.AudioStream | None, audio_bsf: av.BitStreamFilter | None, stream_state: StreamState, stream_settings: StreamSettings) -> None:
        """Initialize StreamMuxer."""
        ...
    
    def make_new_av(self, memory_file: BytesIO, sequence: int, input_vstream: av.video.VideoStream, input_astream: av.audio.stream.AudioStream | None) -> tuple[av.container.OutputContainer, av.video.VideoStream, av.audio.stream.AudioStream | None,]:
        """Make a new av OutputContainer and add output streams."""
        ...
    
    def reset(self, video_dts: int) -> None:
        """Initialize a new stream segment."""
        ...
    
    def mux_packet(self, packet: av.Packet) -> None:
        """Mux a packet to the appropriate output stream."""
        ...
    
    def create_segment(self) -> None:
        """Create a segment when the moov is ready."""
        ...
    
    def check_flush_part(self, packet: av.Packet) -> None:
        """Check for and mark a part segment boundary and record its duration."""
        ...
    
    def flush(self, packet: av.Packet, last_part: bool) -> None:
        """Output a part from the most recent bytes in the memory_file.

        If last_part is True, also close the segment, give it a duration,
        and clean up the av_output and memory_file.
        There are two different ways to enter this function, and when
        last_part is True, packet has not yet been muxed, while when
        last_part is False, the packet has already been muxed. However,
        in both cases, packet is the next packet and is not included in
        the Part.
        This function writes the duration metadata for the Part and
        for the Segment. However, as the fragmentation done by ffmpeg
        may result in fragment durations which fall outside the
        [0.85x,1.0x] tolerance band allowed by LL-HLS, we need to fudge
        some durations a bit by reporting them as being within that
        range.
        Note that repeated adjustments may cause drift between the part
        durations in the metadata and those in the media and result in
        playback issues in some clients.
        """
        ...
    
    def close(self) -> None:
        """Close stream buffer."""
        ...
    


class PeekIterator(Iterator):
    """An Iterator that may allow multiple passes.

    This may be consumed like a normal Iterator, however also supports a
    peek() method that buffers consumed items from the iterator.
    """
    def __init__(self, iterator: Iterator[av.Packet]) -> None:
        """Initialize PeekIterator."""
        ...
    
    def __iter__(self) -> Self:
        """Return an iterator."""
        ...
    
    def __next__(self) -> av.Packet:
        """Return and consume the next item available."""
        ...
    
    def peek(self) -> Generator[av.Packet, None, None]:
        """Return items without consuming from the iterator."""
        ...
    


class TimestampValidator:
    """Validate ordering of timestamps for packets in a stream."""
    def __init__(self, inv_video_time_base: int, inv_audio_time_base: int) -> None:
        """Initialize the TimestampValidator."""
        ...
    
    def is_valid(self, packet: av.Packet) -> bool:
        """Validate the packet timestamp based on ordering within the stream."""
        ...
    


def is_keyframe(packet: av.Packet) -> Any:
    """Return true if the packet is a keyframe."""
    ...

def get_audio_bitstream_filter(packets: Iterator[av.Packet], audio_stream: Any) -> av.BitStreamFilterContext | None:
    """Return the aac_adtstoasc bitstream filter if ADTS AAC is detected."""
    ...

def stream_worker(source: str, pyav_options: dict[str, str], stream_settings: StreamSettings, stream_state: StreamState, keyframe_converter: KeyFrameConverter, quit_event: Event) -> None:
    """Handle consuming streams."""
    ...

