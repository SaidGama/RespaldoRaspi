from fractions import Fraction
from typing import Any, Dict, List, Optional, Sequence, cast

from .frame import Frame

class AVError(Exception): ...

class CodecContext:
    bit_rate: int
    framerate: Fraction
    height: int
    options: Dict[str, str]
    pix_fmt: str
    time_base: Fraction
    width: int
    @staticmethod
    def create(codec: str, mode: Optional[str] = ...) -> CodecContext: ...
    def decode(self, packet: Packet) -> List[Frame]: ...
    def encode(self, frame: Frame) -> List[Packet]: ...
    def open(self) -> None: ...

class Packet:
    pts: int
    time_base: Fraction
    def __init__(self, data: bytes) -> None: ...
    def __bytes__(self) -> bytes: ...

class AudioFormat:
    @property
    def name(self) -> str: ...

class AudioFrame(Frame):
    sample_rate: int
    def __init__(self, format: str = ..., layout: str = ..., samples: int = ...): ...
    @property
    def format(self) -> AudioFormat: ...
    @property
    def layout(self) -> AudioLayout: ...
    @property
    def planes(self) -> Sequence[AudioPlane]: ...

class AudioLayout:
    @property
    def channels(self) -> Sequence[object]: ...
    @property
    def name(self) -> str: ...

class AudioPlane:
    def __bytes__(self) -> bytes: ...
    @property
    def buffer_ptr(self) -> Any: ...
    @property
    def buffer_size(self) -> int: ...
    def update(self, data: bytes) -> None: ...

class VideoFormat:
    @property
    def name(self) -> str: ...

class VideoFrame(Frame):
    def __init__(self, width: int = ..., height: int = ..., format: str = ...): ...
    @property
    def format(self) -> VideoFormat: ...
    @property
    def height(self) -> int: ...
    @property
    def planes(self) -> Sequence[VideoPlane]: ...
    @property
    def width(self) -> int: ...
    def reformat(
        self,
        width: Optional[int] = ...,
        height: Optional[int] = ...,
        format: Optional[Any] = ...,
    ) -> VideoFrame: ...

class VideoPlane:
    @property
    def buffer_ptr(self) -> Any: ...
    @property
    def buffer_size(self) -> int: ...
    @property
    def line_size(self) -> int: ...
    def update(self, data: bytes) -> None: ...