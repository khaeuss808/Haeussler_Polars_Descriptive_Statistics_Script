
import pandas as pd

def readcsv(csvurl):
    return pd.read_csv(csvurl)

def get_summary_stats(dataset):
    return dataset.describe(include='all')



    