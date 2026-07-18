from __future__ import annotations

import sys
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from analysis import sensitivity, validate_matrix, weighted_scores


class WorkflowDecisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.matrix = pd.read_csv(ROOT / "data/reference/decision_matrix.csv")

    def test_weights_and_scores_are_valid(self) -> None:
        validate_matrix(self.matrix)
        scores = weighted_scores(self.matrix)
        self.assertTrue(scores.between(0, 100).all())
        self.assertGreater(scores["ai_assisted"], scores["fully_automated"])

    def test_sensitivity_is_deterministic(self) -> None:
        first = sensitivity(self.matrix, draws=100, seed=7)
        second = sensitivity(self.matrix, draws=100, seed=7)
        pd.testing.assert_frame_equal(first, second)

    def test_bad_weights_are_rejected(self) -> None:
        invalid = self.matrix.copy()
        invalid.loc[0, "weight"] = 0.5
        with self.assertRaisesRegex(ValueError, "sum to one"):
            validate_matrix(invalid)


if __name__ == "__main__":
    unittest.main()
