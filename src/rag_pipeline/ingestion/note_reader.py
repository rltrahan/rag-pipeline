from pathlib import Path

import frontmatter

from rag_pipeline.models import ParsedNote


def read_note(path: str | Path) -> ParsedNote:
    """Read an Obsidian note and return its frontmatter and content."""
    path = Path(path)
    post = frontmatter.load(path)

    return ParsedNote(
        path=path,
        title=post.metadata.get("title", path.stem),
        metadata=post.metadata,
        content=post.content,
    )
