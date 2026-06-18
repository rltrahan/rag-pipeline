"""Basic sanity tests for the rag_pipeline package."""

from rag_pipeline import ingestion


def test_package_imports():
    """Verify that the main package can be imported."""
    import rag_pipeline

    assert rag_pipeline is not None


def test_submodules_exist():
    """Verify expected submodules can be imported."""
    from rag_pipeline import ingestion, retrieval, utils

    assert ingestion is not None
    assert retrieval is not None
    assert utils is not None
