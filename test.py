from main import get_summary_stats

import polars as pl
from pytest import approx


def test_get_summary_stats():
    summary_stats = get_summary_stats(
        pl.read_csv("StudentPerformanceFactors.csv"), "Exam_Score"
    )
    mean = summary_stats.filter(summary_stats["statistic"] == "mean")["value"][0]
    median = summary_stats.filter(summary_stats["statistic"] == "50%")["value"][0]
    std_dev = summary_stats.filter(summary_stats["statistic"] == "std")["value"][0]

    assert mean == approx(67.235659, rel=1e-2)
    assert median == 67
    assert std_dev == approx(3.890456, rel=1e-2)


test_get_summary_stats()
