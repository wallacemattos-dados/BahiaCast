import pandas as pd

def load_data():
    return pd.read_json("data/billboard.json")

def filter_data(df, month, year):
    return df[(df["month"] == month) & (df["year"] == year)]