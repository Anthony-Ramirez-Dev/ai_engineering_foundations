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
                "url": repo["html_url"],
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
            "top_repository": "None",
            "top_repository_stars": 0,
        }

    languages = df["language"].value_counts()
    top_repo = df.sort_values("stars", ascending=False).iloc[0]

    return {
        "repository_count": len(df),
        "total_stars": int(df["stars"].sum()),
        "total_forks": int(df["forks"].sum()),
        "top_language": languages.index[0],
        "top_repository": top_repo["name"],
        "top_repository_stars": int(top_repo["stars"]),
    }
