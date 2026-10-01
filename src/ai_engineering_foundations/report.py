from pathlib import Path

import pandas as pd


def create_markdown_report(
    username: str,
    df: pd.DataFrame,
    summary: dict,
    output_path: str = "output/github_report.md",
) -> Path:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    top_repositories = df.sort_values(
        ["stars", "forks"],
        ascending=False,
    ).head(5)

    language_counts = df["language"].value_counts()

    lines = [
        f"# GitHub Analysis: {username}",
        "",
        "## Summary",
        "",
        f"- Repositories: {summary['repository_count']}",
        f"- Total stars: {summary['total_stars']}",
        f"- Total forks: {summary['total_forks']}",
        f"- Top language: {summary['top_language']}",
        (
            f"- Top repository: {summary['top_repository']}"
            f"({summary['top_repository_stars']} stars)"
        ),
        "",
        "## Languages",
        "",
    ]

    for language, count in language_counts.items():
        lines.append(f"- {language}: {count}")

    lines.extend(
        [
            "",
            "## Top Repositories",
            "",
            "| Repository | Language | Stars | Forks |",
            "|---|---|---:|---:|",
        ]
    )

    for _, repo in top_repositories.iterrows():
        lines.append(
            f"| [{repo['name']}]({repo['url']}) "
            f"| {repo['language']} "
            f"| {repo['stars']} "
            f"| {repo['forks']} |"
        )

    lines.extend(
        [
            "",
            "## Language Visualization",
            "",
            "![GitHub Repository Languages](github_languages.png)",
            "",
        ]
    )

    output.write_text("\n".join(lines), encoding="utf-8")

    return output
