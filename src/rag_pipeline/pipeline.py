from pathlib import Path

from rag_pipeline.ingestion.chunker import chunk_by_headers
from rag_pipeline.ingestion.note_reader import read_note
from rag_pipeline.models import Chunk


def ingest_note(path: str | Path) -> list[Chunk]:
    """Read a note and split it into chunks."""
    note = read_note(path)
    chunks = chunk_by_headers(note)
    return chunks
