from main import (
    get_summary_stats
)

import pandas as pd

from pytest import approx

def test_get_summary_stats():
    summary_stats= get_summary_stats(pd.read_csv("StudentPerformanceFactors.csv"), "Exam_Score")
    assert summary_stats["mean"] == approx(67.235659, rel=1e-2)
    assert summary_stats["50%"] == 67
    assert summary_stats["std"] == approx(3.890456, rel=1e-2)


test_get_summary_stats()
