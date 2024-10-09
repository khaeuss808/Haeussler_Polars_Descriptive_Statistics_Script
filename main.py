"""Main Python file"""

import polars as pl
import matplotlib.pyplot as plt
import seaborn as sns


def readcsv(filename):
    return pl.read_csv(filename)


def describe_it(dataset):
    return dataset.describe()


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


def save_to_md(data):  # for autogenerating report
    # Select a subset of columns to keep the markdown readable
    subset_cols = ["Hours_Studied", "Attendance", "Sleep_Hours", "Exam_Score"]
    data_subset = data.select(subset_cols)
    test = describe_it(data_subset).to_pandas()  # Convert to pandas for markdown

    # Convert the table to markdown
    mkdown = test.to_markdown(index=False)

    # Get summary statistics for "Exam_Score"
    test2 = get_summary_stats(data, "Exam_Score")

    # Convert summary statistics to pandas DataFrame and then to markdown
    summary_stats_df = test2.to_pandas()  # Convert summary stats to pandas DataFrame
    mkdown2 = summary_stats_df.to_markdown(index=False)

    # Save markdown output to a file
    with open("Student_Summary_Report.md", "a", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(mkdown + "\n\n")  # Write description of selected columns
        file.write("Summarize Student Final Exam Scores:\n")
        file.write(mkdown2)  # Write summary of Exam_Score


if __name__ == "__main__":
    # read the csv
    student_data = readcsv("StudentPerformanceFactors.csv")

    # get summary stats: mean, median, sd
    summary_stats = get_summary_stats(student_data, "Exam_Score")
    print(summary_stats)

    # autogenerate markdown
    save_to_md(student_data)

    # create visualizations
    create_histogram(student_data, "Exam_Score")
    create_scatter(student_data, "Hours_Studied", "Exam_Score")
