import pandas as pd


def repositories_to_dataframe(repositories: list[dict]) -> pd.DataFrame:
    rows = []

    for repo in repositories:
        rows.append(
            {
                "name": repo["name"],
                "language": repo.get("language") or "Unknown",
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"],
                "open_issues": repo["open_issues_count"],
            }
        )

    return pd.DataFrame(rows)


def summarize_repositories(df: pd.DataFrame) -> dict:
    if df.empty:
        return {
            "repository_count": 0,
            "total_stars": 0,
            "total_forks": 0,
            "top_language": "None",
        }

    languages = df["language"].value_counts()

    return {
        "repository_count": len(df),
        "total_stars": int(df["stars"].sum()),
        "total_forks": int(df["forks"].sum()),
        "top_language": languages.index[0],
    }
