from requests import RequestException

from ai_engineering_foundations import greet
from ai_engineering_foundations.report import create_markdown_report
from ai_engineering_foundations.visualization import create_language_chart


def show_github_profile() -> None:
    username = input("GitHub username: ").strip()

    try:
        profile = get_github_profile(username)
    except RequestException as error:
        print(f"Unable to retrieve GitHub profile: {error}")
        return

    print()
    print("GitHub Profile")
    print("---------------")
    print(f"Username: {profile['login']}")
    print(f"Name: {profile.get('name') or 'Not provided'}")
    print(f"Public repositories: {profile['public_repos']}")
    print(f"Followers: {profile['followers']}")
    print(f"Following: {profile['following']}")


def main() -> None:
    print("AI Engineering Foundations")
    print("---------------------------")
    print("1. Greeting")
    print("2. GitHub profile lookup")
    print("3. GitHub repository analysis")
    print("4. Train repository ML model")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Enter your name: ")
        print(greet(name))
    elif choice == "2":
        show_github_profile()
    elif choice == "3":
        analyze_github_repositories()
    elif choice == "4":
        train_repository_model()
    elif choice == "5":
        print("Goodbye!")
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()

from ai_engineering_foundations.analysis import (
    repositories_to_dataframe,
    summarize_repositories,
)
from ai_engineering_foundations.github_client import (
    get_github_profile,
    get_github_repositories,
)
from ai_engineering_foundations.ml import train_star_model


def train_repository_model() -> None:
    username = input("GitHub username for training data: ").strip()

    try:
        repositories = get_github_repositories(username)
    except RequestException as error:
        print(f"Unable to retrieve repositories: {error}")
        return

    df = repositories_to_dataframe(repositories)

    try:
        _, metrics = train_star_model(df)
    except ValueError as error:
        print(f"Unable to train model: {error}")
        return

    print()
    print("Machine Learning Results")
    print("------------------------")
    print(f"Training samples: {metrics['training_samples']}")
    print(f"Testing samples: {metrics['testing_samples']}")
    print(f"Mean absolute error: {metrics['mae']:.2f}")
    print(f"R2 score: {metrics['r2']:.2f}")


def analyze_github_repositories() -> None:
    username = input("GitHub username: ").strip()

    try:
        repositories = get_github_repositories(username)
    except RequestException as error:
        print(f"Unable to retrieve repositories: {error}")
        return

    df = repositories_to_dataframe(repositories)
    summary = summarize_repositories(df)
    chart_path = create_language_chart(df)
    report_path = create_markdown_report(username, df, summary)

    print()
    print("Repository Analysis")
    print("-------------------")
    print(f"Repositories: {summary['repository_count']}")
    print(f"Total stars: {summary['total_stars']}")
    print(f"Total forks: {summary['total_forks']}")
    print(f"Top language: {summary['top_language']}")
    print(f"Chart saved to: {chart_path}")
    print(f"Report saved to: {report_path}")
