
import pandas as pd


def load_csv(file):
    df=pd.read_csv(file)
    if df.empty:
        return None, "The CSV Is Empty!!"
    return df, None

def data_cleaner(df):
    clean_df = df.dropna()
    if clean_df.empty:
        return None, "The DataFrame is empty after cleaning."

    return clean_df, None


