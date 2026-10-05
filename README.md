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
- Random Forest model for repository star prediction
- Training evaluation with mean absolute error and R2
- Saved model artifacts and versioned metadata
- Metadata validation before prediction
- Prediction input validation
- Feature importance output

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
│       ├── ml.py
│       ├── report.py
│       └── visualization.py
├── tests/
│   ├── test_github_client.py
│   ├── test_greet.py
│   ├── test_ml.py
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
git clone https://github.com/Anthony-Ramirez-Dev/ai_engineering_foundations.git
cd ai_engineering_foundations
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
4. Train repository ML model
5. Predict repository stars
6. Exit
```

Selecting repository analysis retrieves live GitHub data and generates:

```text
output/github_languages.png
output/github_report.md
```

## Architecture

```text
GitHub REST API
    ↓
Repository data → pandas DataFrame
    ├── Statistics → language chart + Markdown report
    └── Train/test split → Random Forest model
                              ├── Evaluation metrics
                              ├── Feature importance
                              └── Saved model + metadata

Prediction inputs → input validation → model prediction
```

## Machine Learning Workflow

Choose option 4 and enter a public GitHub username.
Training requires at least 10 repositories.

The application splits the data into 75% training and 25% testing,
trains a Random Forest regressor, and reports evaluation metrics
and feature importance.

Training saves:

```text
models/star_predictor.joblib
models/star_predictor_metadata.json
```

Choose option 5 to predict stars using forks, open issues,
repository size, archived status, and whether issues are enabled.

The application validates model metadata before prediction and
rejects negative forks, open issues, and repository size.

## Example Output

One training run using public Microsoft repository data produced:

```text
Training samples: 75
Testing samples: 25
Mean absolute error: 22321.80
R2 score: 0.52

Feature Importance
------------------
forks: 87.4%
size: 8.2%
open_issues: 4.4%
archived: 0.0%
has_issues: 0.0%
```

Results vary with the retrieved repositories and training data.

Invalid prediction input produces a message such as:

```text
Invalid input: Forks cannot be negative.
```

## Model Limitations

This model is a learning exercise. Its predictions are estimates,
and the example run's mean absolute error was about 22,322 stars.

Data from one GitHub account may not represent repositories from
other accounts. Results also depend on the repositories returned
by the API.

Feature importance describes how the trained forest uses each
input. It does not establish causation or show whether an input
increases or decreases predicted stars.

The model uses a single train/test split. Further evaluation would
include cross-validation and comparison with a simple baseline.

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
- Train/test splitting and model evaluation
- Model persistence and metadata validation
- Feature importance and model limitations
- Boundary testing and prediction input validation

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
- AI model integration
- Automated portfolio analysis
- Web interface

## Author

Antwon Ramirez

Software Development / AI Software Engineering student building practical projects through independent study.