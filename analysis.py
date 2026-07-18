from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
MODEL_COLUMNS = ("ai_assisted", "fully_automated")


def validate_matrix(frame: pd.DataFrame) -> None:
    required = {"criterion", "weight", *MODEL_COLUMNS}
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    if not np.isclose(frame["weight"].sum(), 1.0):
        raise ValueError("Weights must sum to one.")
    if not frame[list(MODEL_COLUMNS)].apply(lambda s: s.between(0, 100).all()).all():
        raise ValueError("Model scores must be between 0 and 100.")


def weighted_scores(frame: pd.DataFrame) -> pd.Series:
    validate_matrix(frame)
    return frame[list(MODEL_COLUMNS)].multiply(frame["weight"], axis=0).sum()


def sensitivity(frame: pd.DataFrame, draws: int = 10_000, seed: int = 42) -> pd.DataFrame:
    """Vary criterion weights uniformly over the simplex and compare models."""

    validate_matrix(frame)
    if draws <= 0:
        raise ValueError("draws must be positive")
    rng = np.random.default_rng(seed)
    weights = rng.dirichlet(np.ones(len(frame)), size=draws)
    values = frame[list(MODEL_COLUMNS)].to_numpy(dtype=float)
    scores = weights @ values
    winner = np.where(scores[:, 0] >= scores[:, 1], MODEL_COLUMNS[0], MODEL_COLUMNS[1])
    return pd.DataFrame({"ai_assisted_score": scores[:, 0], "fully_automated_score": scores[:, 1], "winner": winner})


def main() -> None:
    matrix = pd.read_csv(ROOT / "data/reference/decision_matrix.csv")
    scores = weighted_scores(matrix)
    simulations = sensitivity(matrix)
    win_rate = simulations["winner"].value_counts(normalize=True).rename("win_rate")

    tables = ROOT / "outputs/tables"
    figures = ROOT / "outputs/figures"
    tables.mkdir(parents=True, exist_ok=True)
    figures.mkdir(parents=True, exist_ok=True)
    scores.rename("weighted_score").to_csv(tables / "model_scores.csv")
    win_rate.to_csv(tables / "sensitivity_win_rates.csv")

    labels = ["AI-assisted first", "Fully automated"]
    fig, ax = plt.subplots(figsize=(7.5, 4.8))
    bars = ax.bar(labels, scores.values, color=["#6741D9", "#A78BFA"])
    ax.bar_label(bars, labels=[f"{value:.1f}" for value in scores.values], padding=4)
    ax.set(title="A phased AI-assisted model balances value and deliverability", ylabel="Weighted decision score / 100", ylim=(0, 100))
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    fig.savefig(figures / "model_scores.png", dpi=180, facecolor="white")
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7.5, 4.8))
    values = [win_rate.get(name, 0) * 100 for name in MODEL_COLUMNS]
    bars = ax.bar(labels, values, color=["#6741D9", "#A78BFA"])
    ax.bar_label(bars, labels=[f"{value:.1f}%" for value in values], padding=4)
    ax.set(title="Recommendation sensitivity to alternative criterion weights", ylabel="Share of 10,000 draws preferred (%)", ylim=(0, 100))
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    fig.savefig(figures / "sensitivity.png", dpi=180, facecolor="white")
    plt.close(fig)

    print(scores)
    print(win_rate)


if __name__ == "__main__":
    main()
