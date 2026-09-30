from unittest.mock import Mock, patch

from ai_engineering_foundations.github_client import get_github_profile


@patch("ai_engineering_foundations.github_client.requests.get")
def test_get_github_profile(mock_get):
    fake_response = Mock()

    fake_response.json.return_value = {
        "login": "testuser",
        "name": "Test user",
        "public_repos": 10,
        "followers": 20,
        "following": 5,
    }

    mock_get.return_value = fake_response

    profile = get_github_profile("testuser")

    assert profile["login"] == "testuser"
    assert profile["public_repos"] == 10

    mock_get.assert_called_once_with(
        "https://api.github.com/users/testuser", timeout=10
    )
