"""Main Python file"""

import polars as pl
import matplotlib.pyplot as plt
import seaborn as sns


def readcsv(filename):
    return pl.read_csv(filename)


def get_summary_stats(dataset, col_of_intrst):
    summ_stats = dataset[col_of_intrst].describe()

    # Use filter to get the specific rows for mean, median, and std
    mean = summ_stats.filter(summ_stats["statistic"] == "mean")["value"][0]
    median = summ_stats.filter(summ_stats["statistic"] == "50%")["value"][
        0
    ]  # 50% corresponds to the median
    std_dev = summ_stats.filter(summ_stats["statistic"] == "std")["value"][0]

    print("Mean final exam score is " + str(round(mean, 3)) + " minutes")
    print("Median final exam score is " + str(round(median, 3)) + " minutes")
    print(
        "Standard Deviation of final exam score is "
        + str(round(std_dev, 3))
        + " minutes"
    )

    return summ_stats


def create_histogram(df, col_of_intrst):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[col_of_intrst].drop_nans(), bins=30, kde=True)
    plt.title("Histogram of Final Exam Scores")
    plt.xlabel("Exam Score (out of 100)")
    plt.ylabel("Frequency")
    plt.show()


def create_scatter(data, x_col, y_col):
    plt.scatter(data[x_col].to_list(), data[y_col].to_list())
    plt.title(x_col + " vs. " + y_col)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()


if __name__ == "__main__":
    # read the csv
    student_data = readcsv("StudentPerformanceFactors.csv")

    # get summary stats: mean, median, sd
    summary_stats = get_summary_stats(student_data, "Exam_Score")
    print(summary_stats)

    # create visualizations
    create_histogram(student_data, "Exam_Score")
    create_scatter(student_data, "Hours_Studied", "Exam_Score")
