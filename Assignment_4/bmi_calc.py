"""
This program calculates BMI and assigns a health category.
It adds new columns to a DataFrame for analysis.
"""

import pandas as pd


def bmi_status(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi <= 24.9:
        return "healthy"
    elif bmi <= 29.9:
        return "overweight"
    elif bmi <= 34.9:
        return "high risk of diabetes"
    else:
        return "critical health condition"


def add_bmi(df):
    df["BMI"] = df["weight"] / df["height"]
    df["Health_Status"] = df["BMI"].apply(bmi_status)
    print(df)


def run():
    try:
        df = pd.read_csv("health_data.csv")
        add_bmi(df)
    except FileNotFoundError:
        print("CSV file not found")


if __name__ == "__main__":
    run()