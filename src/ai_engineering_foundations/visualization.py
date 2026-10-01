from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def create_language_chart(
    df: pd.DataFrame,
    output_path: str = "output/github_languages.png",
) -> Path:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    if df.empty:
        raise ValueError("Cannot create chart from an empty DataFrame.")

    language_counts = df["language"].value_counts()

    plt.figure(figsize=(8, 5))
    language_counts.plot(kind="bar")

    plt.title("GitHub Repository Languages")
    plt.xlabel("Language")
    plt.ylabel("Repositories")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig(output)
    plt.close()

    return output
