# AI Engineering Foundations

A Python portfolio project focused on practical software engineering, data analysis, API integration, testing, visualization, and automation.

## Overview

This project analyzes public GitHub repository data through the GitHub REST API.

It retrieves repository information, processes the response with pandas, calculates useful statistics, generates a visualization, and creates a Markdown report.

The project is also used as a hands-on environment for learning professional Python development practices.

## Features

- Interactive command-line interface
- GitHub profile lookup
- GitHub repository analysis
- REST API integration
- JSON processing
- pandas DataFrame transformation
- Repository statistics and rankings
- Programming language analysis
- Matplotlib visualization
- Markdown report generation
- Automated testing with pytest
- Code quality checks with Ruff
- Dependency management with uv
- Continuous integration with GitHub Actions

## Tech Stack

- Python 3.14
- uv
- pandas
- NumPy
- Matplotlib
- Requests
- scikit-learn
- pytest
- Ruff
- Git
- GitHub Actions

## Project Structure

```text
ai-engineering-foundations/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── ai_engineering_foundations/
│       ├── __init__.py
│       ├── analysis.py
│       ├── github_client.py
│       ├── main.py
│       ├── report.py
│       └── visualization.py
├── tests/
│   ├── test_analysis.py
│   ├── test_github_client.py
│   ├── test_greet.py
│   ├── test_report.py
│   └── test_visualization.py
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
└── uv.lock
```

## Installation

Clone the repository:

```bash
git clone https://github.com/anthonyramirez82214-alt/ai-engineering-foundations.git
cd ai-engineering-foundations
```

Install the project dependencies:

```bash
uv sync
```

## Running the Application

Start the CLI:

```bash
uv run ai_engineering_foundations
```

The application provides options for:

```text
1. Greeting
2. GitHub profile lookup
3. GitHub repository analysis
4. Exit
```

Selecting repository analysis retrieves live GitHub data and generates:

```text
output/github_languages.png
output/github_report.md
```

## Running Tests

Run the complete test suite:

```bash
uv run pytest -v
```

## Code Quality

Run Ruff:

```bash
uv run ruff check .
```

Format the project:

```bash
uv run ruff format .
```

## Continuous Integration

GitHub Actions automatically runs the project's quality checks when code is pushed to the `main` branch or submitted through a pull request.

The CI pipeline:

1. Checks out the repository
2. Configures Python
3. Installs uv
4. Installs project dependencies
5. Runs Ruff
6. Runs pytest

## What I Am Learning

This project is part of my independent study in AI software engineering and software development.

Topics practiced include:

- Python package design
- Virtual environments and dependency management
- REST APIs
- HTTP request handling
- JSON parsing
- pandas data processing
- Data visualization
- Error handling
- Unit testing
- Mocking external API requests
- Git and GitHub workflows
- Continuous integration
- Code organization and maintainability

## Development Workflow

Before committing changes:

```bash
uv run ruff check .
uv run pytest
git status
```

Then:

```bash
git add .
git commit -m "Describe the change"
git push
```

## Planned Improvements

Future development may include:

- Expanded repository metrics
- Additional visualizations
- CSV and JSON export
- Improved CLI design
- GitHub API authentication
- Machine learning features
- AI model integration
- Automated portfolio analysis
- Web interface

## Author

Antwon Ramirez

Software Development / AI Software Engineering student building practical projects through independent study.