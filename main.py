"""Main Python file"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def readcsv(filename):
    return pd.read_csv(filename)

def get_summary_stats(dataset, col_of_intrst):
    summ_stats = dataset[col_of_intrst].describe()
    print("Mean final exam score  is " + str(round(summ_stats["mean"], 3)) + " minutes")
    print("Median final exam score is "+ str(round(summ_stats["50%"], 3)) + " minutes")
    print("Standard Deviation of final exam score is " + str(round(summ_stats["std"], 3)) + " minutes")

    return summ_stats

def create_histogram(df, col_of_intrst): 
    plt.figure(figsize=(10, 6))
    sns.histplot(df[col_of_intrst].dropna(), bins=30, kde=True)
    plt.title('Histogram of Final Exam Scores')
    plt.xlabel("Exam Score (out of 100)")
    plt.ylabel('Frequency')
    plt.show()

def create_scatter(data, x_col, y_col):
    data.plot.scatter(x = x_col, y= y_col)
    plt.title(x_col +" vs. "+ y_col)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show() 


if __name__ == "__main__":
    # read the csv
    student_data= readcsv("StudentPerformanceFactors.csv")

    # get summary stats: mean, median, sd
    summary_stats = get_summary_stats(student_data, "Exam_Score")
    print(summary_stats)

    # create visualizations
    create_histogram(student_data, "Exam_Score")
    create_scatter(student_data, "Hours_Studied", "Exam_Score")
