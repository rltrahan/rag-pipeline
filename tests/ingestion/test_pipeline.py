from pathlib import Path
from unittest.mock import patch

import pytest

from rag_pipeline.models import Chunk, ParsedNote
from rag_pipeline.pipeline import ingest_note


@pytest.fixture
def sample_parsed_note():
    return ParsedNote(
        path=Path("test.md"),
        title="Test Note",
        metadata={"tags": ["test"]},
        content="# Header 1\nSome content here\n## Subheader\nMore content",
    )


@pytest.fixture
def sample_chunks():
    return [
        Chunk(
            content="Header 1\nSome content here",
            metadata={"breadcrumb": "Header 1", "source_file": "test.md"},
            chunk_index=0,
        ),
        Chunk(
            content="Subheader\nMore content",
            metadata={"breadcrumb": "Header 1 > Subheader", "source_file": "test.md"},
            chunk_index=1,
        ),
    ]


@patch("rag_pipeline.pipeline.read_note")
@patch("rag_pipeline.pipeline.chunk_by_headers")
def test_ingest_note_calls_read_note_then_chunk_by_headers(
    mock_chunk_by_headers, mock_read_note, sample_parsed_note, sample_chunks
):
    """ingest_note should read the note and then pass the ParsedNote to the chunker."""
    mock_read_note.return_value = sample_parsed_note
    mock_chunk_by_headers.return_value = sample_chunks

    result = ingest_note("some/path/note.md")

    mock_read_note.assert_called_once_with("some/path/note.md")
    mock_chunk_by_headers.assert_called_once_with(sample_parsed_note)
    assert result == sample_chunks


@patch("rag_pipeline.pipeline.read_note")
@patch("rag_pipeline.pipeline.chunk_by_headers")
def test_ingest_note_returns_empty_list_when_chunker_returns_empty(
    mock_chunk_by_headers, mock_read_note, sample_parsed_note
):
    mock_read_note.return_value = sample_parsed_note
    mock_chunk_by_headers.return_value = []

    result = ingest_note(Path("empty.md"))

    assert result == []


def test_ingest_note_end_to_end_with_real_test_note():
    """Light integration test using your existing test_note.md."""
    test_file = Path(__file__).parent / "test_note.md"

    chunks = ingest_note(str(test_file))

    assert isinstance(chunks, list)
    assert all(isinstance(c, Chunk) for c in chunks)
    assert len(chunks) > 0

    # Basic sanity checks on the first chunk
    first = chunks[0]
    assert first.chunk_index == 0
    assert "source_file" in first.metadata
    assert "breadcrumb" in first.metadata
