from rag_pipeline.ingestion.chunker import chunk_by_headers
from rag_pipeline.models import Chunk, ParsedNote


def test_chunk_by_headers():

    test_data = ParsedNote(
        path="test_file.md",
        title="Test Title",
        metadata={},
        content="# Header 1\nContent under header 1\nMulti-line content\n## Subheader 1.1\nContent under subheader 1.1\n# Header 2\nContent under header 2",
    )

    chunked = chunk_by_headers(test_data)

    assert isinstance(chunked, list)
    assert all(isinstance(chunk, Chunk) for chunk in chunked)
    assert len(chunked) == 3
    assert chunked[0].content == "Header 1\nContent under header 1\nMulti-line content"
    assert chunked[0].metadata["breadcrumb"] == "Header 1"
    assert chunked[0].metadata["source_file"] == "test_file.md"
    assert chunked[0].chunk_index == 0

    assert chunked[1].content == "Subheader 1.1\nContent under subheader 1.1"

    assert chunked[1].metadata["breadcrumb"] == "Header 1 > Subheader 1.1"
    assert chunked[1].metadata["source_file"] == "test_file.md"
    assert chunked[1].chunk_index == 1

    assert chunked[2].content == "Header 2\nContent under header 2"

    assert chunked[2].metadata["breadcrumb"] == "Header 2"
    assert chunked[2].metadata["source_file"] == "test_file.md"
    assert chunked[2].chunk_index == 2

    test_data = ParsedNote(
        path="test_file.md",
        title="Test Title",
        metadata={},
        content="Test initial section without header\n## Subheader 1.1\nContent under subheader 1.1\n# Header 2\nContent under header 2",
    )

    chunked = chunk_by_headers(test_data)

    assert len(chunked) == 3
    assert chunked[0].content == "Test initial section without header"
    assert chunked[0].metadata["breadcrumb"] == "Test Title"
    assert chunked[0].metadata["source_file"] == "test_file.md"
    assert chunked[0].chunk_index == 0

    assert chunked[1].content == "Subheader 1.1\nContent under subheader 1.1"
    assert chunked[1].metadata["breadcrumb"] == "Subheader 1.1"
    assert chunked[1].metadata["source_file"] == "test_file.md"
    assert chunked[1].chunk_index == 1

    assert chunked[2].content == "Header 2\nContent under header 2"

    assert chunked[2].metadata["breadcrumb"] == "Header 2"
    assert chunked[2].metadata["source_file"] == "test_file.md"
    assert chunked[2].chunk_index == 2

    test_data = ParsedNote(
        path="test_file.md",
        title="Test Title",
        metadata={},
        content="## Subheader 1\nTest initial section as subsection\n## Subheader 1.1\nContent under subheader 1.1\n# Header 2\nContent under header 2",
    )

    chunked = chunk_by_headers(test_data)

    assert len(chunked) == 3
    assert chunked[0].content == "Subheader 1\nTest initial section as subsection"

    assert chunked[0].metadata["breadcrumb"] == "Subheader 1"
    assert chunked[0].metadata["source_file"] == "test_file.md"
    assert chunked[0].chunk_index == 0

    assert chunked[1].content == "Subheader 1.1\nContent under subheader 1.1"

    assert chunked[1].metadata["breadcrumb"] == "Subheader 1.1"
    assert chunked[1].metadata["source_file"] == "test_file.md"
    assert chunked[1].chunk_index == 1

    assert chunked[2].content == "Header 2\nContent under header 2"

    assert chunked[2].metadata["breadcrumb"] == "Header 2"
    assert chunked[2].metadata["source_file"] == "test_file.md"
    assert chunked[2].chunk_index == 2
