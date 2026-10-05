import json
from datetime import UTC, datetime
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

MODEL_VERSION = "1.0.0"

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


def load_model_metadata(
    metadata_path: str = "models/star_predictor_metadata.json",
) -> dict:
    path = Path(metadata_path)

    if not path.exists():
        raise FileNotFoundError(f"Metadata not found: {path}")

    return json.loads(path.read_text(encoding="utf-8"))


def validate_model_metadata(metadata: dict) -> None:
    if metadata.get("model_version") != MODEL_VERSION:
        raise ValueError(
            "model version mismatch: "
            f"expected {MODEL_VERSION}, "
            f"got {metadata.get('model_version')}"
        )

    if metadata.get("model_type") != "RandomForestRegressor":
        raise ValueError(f"Unexpected model type: {metadata.get('model_type')}")

    if metadata.get("target") != TARGET:
        raise ValueError(
            f"Model target mismatch: expected {TARGET}, got {metadata.get('target')}"
        )

    if metadata.get("features") != FEATURES:
        raise ValueError("Model feature schema does not match the application.")


def save_model(
    model: RandomForestRegressor,
    output_path: str = "models/star_predictor.joblib",
) -> Path:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, output)

    return output


def save_model_metadata(
    metrics: dict,
    output_path: str = "models/star_predictor_metadata.json",
) -> Path:
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    metadata = {
        "model_version": MODEL_VERSION,
        "model_type": "RandomForestRegressor",
        "target": TARGET,
        "features": FEATURES,
        "trained_at": datetime.now(UTC).isoformat(),
        "training_samples": metrics["training_samples"],
        "testing_samples": metrics["testing_samples"],
        "mae": float(metrics["mae"]),
        "r2": float(metrics["r2"]),
    }

    output.write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )

    return output


def load_model(
    model_path: str = "models/star_predictor.joblib",
) -> RandomForestRegressor:
    path = Path(model_path)

    if not path.exists():
        raise FileNotFoundError(f"Model not found: {path}")

    return joblib.load(path)


def validate_prediction_inputs(
    forks: int,
    open_issues: int,
    size: int,
) -> None:
    if forks < 0:
        raise ValueError("Forks cannot be negative.")

    if open_issues < 0:
        raise ValueError("Open issues cannot be negative.")

    if size < 0:
        raise ValueError("Repository size cannot be negative.")


def predict_stars(
    model: RandomForestRegressor,
    forks: int,
    open_issues: int,
    size: int,
    archived: bool,
    has_issues: bool,
) -> float:
    validate_prediction_inputs(
        forks=forks,
        open_issues=open_issues,
        size=size,
    )

    features = pd.DataFrame(
        [
            {
                "forks": forks,
                "open_issues": open_issues,
                "size": size,
                "archived": int(archived),
                "has_issues": int(has_issues),
            }
        ]
    )

    predictions = model.predict(features)

    return float(predictions[0])
