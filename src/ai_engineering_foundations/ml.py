import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

FEATURES = [
    "forks",
    "open_issues",
    "size",
    "archived",
    "has_issues",
]

TARGET = "stars"


def prepare_ml_data(df: pd.DataFrame):
    if len(df) < 10:
        raise ValueError("At least 10 repositories are required to train the model.")

    features = df[FEATURES].copy()

    features["archived"] = features["archived"].astype(int)
    features["has_issues"] = features["has_issues"].astype(int)

    target = df[TARGET]

    return features, target


def train_star_model(df: pd.DataFrame):
    features, target = prepare_ml_data(df)

    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.25, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)

    model.fit(x_train, y_train)

    predictions = model.predict(x_test)

    metrics = {
        "mae": mean_absolute_error(y_test, predictions),
        "r2": r2_score(y_test, predictions),
        "training_samples": len(x_train),
        "testing_samples": len(x_test),
    }

    return model, metrics
