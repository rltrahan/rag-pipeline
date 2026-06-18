from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class ParsedNote:
    path: Path
    title: str
    metadata: dict[str, Any]
    content: str


@dataclass
class Chunk:
    content: str
    chunk_index: int
    metadata: dict[str, Any]
