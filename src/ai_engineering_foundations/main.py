from requests import RequestException

from ai_engineering_foundations import greet
from ai_engineering_foundations.github_client import get_github_profile


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
    print("3. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Enter your name: ")
        print(greet(name))
    elif choice == "2":
        show_github_profile()
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
