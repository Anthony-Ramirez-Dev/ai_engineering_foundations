import requests


def get_github_profile(username: str) -> list[dict]:
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


def get_github_repositories(username: str) -> list[dict]:
    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(
        url,
        params={"per_page": 100, "sort": "updated"},
        timeout=10,
    )
    response.raise_for_status()

    return response.json()
