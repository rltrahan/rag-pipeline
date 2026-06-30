from pathlib import Path

from rag_pipeline.ingestion.note_reader import read_note
from rag_pipeline.models import ParsedNote


def test_read_note_with_frontmatter():
    """Test that read_note correctly parses frontmatter and content."""
    # Use a relative path to our test file
    test_file = Path(__file__).parent / "test_note.md"

    result = read_note(str(test_file))

    assert isinstance(result, ParsedNote)
    assert result.path == str(test_file)
    assert result.metadata["title"] == "Test Note"
    assert "test" in result.metadata["tags"]
    assert "This is a test note" in result.content


def test_read_note_without_frontmatter(tmp_path):
    """Test reading a note that has no frontmatter."""
    # Create a temporary file without frontmatter
    note_file = tmp_path / "no_frontmatter.md"
    note_file.write_text("Just some plain content here.")

    result = read_note(str(note_file))

    assert result.metadata == {}
    assert result.content == "Just some plain content here."
