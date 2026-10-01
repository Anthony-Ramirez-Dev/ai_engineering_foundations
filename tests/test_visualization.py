import pandas as pd

from ai_engineering_foundations.visualization import create_language_chart


def test_create_language_chart(tmp_path):
    df = pd.DataFrame(
        {
            "language": [
                "Python",
                "Python",
                "JavaScript",
            ]
        }
    )

    output = tmp_path / "languages.png"

    result = create_language_chart(df, str(output))

    assert result.exists()
    assert result.stat().st_size > 0
