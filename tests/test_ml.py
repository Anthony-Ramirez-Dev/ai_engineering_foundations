import pandas as pd
import pytest

from ai_engineering_foundations.ml import (
    load_model,
    prepare_ml_data,
    save_model,
    train_star_model,
)


def test_save_and_load_model(tmp_path):
    df = make_test_data()

    model, _ = train_star_model(df)

    model_path = tmp_path / "model.joblib"

    saved_path = save_model(model, str(model_path))

    assert saved_path.exists()

    loaded_model = load_model(str(saved_path))

    assert loaded_model is not None


def make_test_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "forks": [0, 1, 2, 1, 3, 0, 4, 2, 1, 5, 3, 2],
            "open_issues": [0, 1, 0, 2, 1, 0, 3, 1, 0, 2, 1, 0],
            "size": [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],
            "archived": [
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ],
            "has_issues": [
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
                True,
            ],
            "stars": [1, 2, 4, 3, 6, 2, 8, 5, 3, 10, 7, 6],
        }
    )


def test_prepare_ml_data():
    df = make_test_data()

    features, target = prepare_ml_data(df)

    assert len(features) == 12
    assert len(target) == 12
    assert "stars" not in features.columns


def test_prepare_ml_data_requires_enough_rows():
    df = make_test_data().head(5)

    with pytest.raises(ValueError):
        prepare_ml_data(df)


def test_train_star_model():
    df = make_test_data()

    model, metrics = train_star_model(df)

    assert model is not None
    assert metrics["training_samples"] == 9
    assert metrics["testing_samples"] == 3
    assert "mae" in metrics
    assert "r2" in metrics
