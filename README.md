# RAG Pipeline

A personal RAG (Retrieval-Augmented Generation) pipeline that uses an Obsidian knowledge vault as a source of truth. The system indexes notes into PostgreSQL + pgvector and enables grounded responses from local LLMs (Ollama).

## Project Goals

- Build a functional Obsidian RAG pipeline
- Establish modern Python development practices
- Learn lightweight CI/CD using GitHub Actions
- Maintain a clean, professional project structure

## Development Setup

### Prerequisites

- Python 3.11 or higher
- Git
- Access to the project’s PostgreSQL + pgvector database
- Access to an Ollama instance (for embeddings and generation)

### Environment Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd rag-pipeline
   ```
2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate          # Linux / macOS
   .venv\Scripts\activate             # Windows
   ```
3. Install the project with development dependencies
   ```bash
   pip install -e ".[dev]"
   ```

4. Configure environment variables
   Copy the example environment file and update it with your settings:
   ```bash
   cp .env.example .env
   ```
   Edit .env and fill in your actual database and Ollama connection details.

## Running Tests
   ```bash
   pytest
   ```
   
## Linting and Formatting
This project uses Ruff for linting and formatting.
   ```bash
   # Check for issues
   ruff check .
   # Format code
   ruff format .
   ```
## Running the CI Pipeline Locally
The same checks that run in GitHub Actions can be executed locally:
   ```bash
   ruff check .
   ruff format --check .
   pytest
   ```

## Project Structure

rag-pipeline/
├── src/rag_pipeline/     # Main application code
├── tests/                # Test files
├── .github/workflows/    # GitHub Actions CI configuration
├── docs/                 # Additional documentation
├── pyproject.toml        # Project configuration and dependencies
├── README.md
└── .env.example

## Continuous Integration
This project uses GitHub Actions for CI. On every push and pull request to main, the pipeline will:
-Set up Python
-Install dependencies
-Run linting and formatting checks
-Run the test suite

See .github/workflows/ci.yml for details.

## License
This is a personal learning project.
