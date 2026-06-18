from langchain_text_splitters import MarkdownHeaderTextSplitter

from rag_pipeline.models import Chunk, ParsedNote


def chunk_by_headers(post: ParsedNote) -> list[Chunk]:
    """
    Split a ParsedNote into chunks using LangChain's MarkdownHeaderTextSplitter.
    Preserves heading hierarchy in metadata.
    """
    headers_to_split_on = [
        ("#", "h1"),
        ("##", "h2"),
        ("###", "h3"),
        ("####", "h4"),
    ]

    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=True,  # Keep headers in the content
    )

    # Split the content
    docs = markdown_splitter.split_text(post.content)

    chunks = []
    for idx, doc in enumerate(docs):
        # Get the most specific (deepest) header from metadata
        header_values = list(doc.metadata.values())
        header_text = header_values[-1] if header_values else ""

        # Build content with clean header at the top
        text = f"{header_text}\n{doc.page_content}" if header_text else doc.page_content

        # Build breadcrumb from all headers in metadata
        breadcrumb = " > ".join(header_values) if header_values else post.title

        chunk = Chunk(
            content=text,
            metadata={
                "source_file": post.path,
                "breadcrumb": breadcrumb,
                **doc.metadata,
            },
            chunk_index=idx,
        )
        chunks.append(chunk)

    return chunks
