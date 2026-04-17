"""
This program reads data from 'health_data.csv' and visualizes
relationships between different health attributes using scatter plots.

It uses Pandas for data handling and Matplotlib for plotting.
"""

import pandas as pd
import matplotlib.pyplot as plt


def load():
    return pd.read_csv("health_data.csv")


def plot(df):

    plt.scatter(df["weight"], df["height"])
    plt.title("Weight vs Height")
    plt.xlabel("weight")
    plt.ylabel("height")
    plt.show()

    plt.scatter(df["age"], df["weight"])
    plt.title("Age vs Weight")
    plt.xlabel("age")
    plt.ylabel("weight")
    plt.show()

    plt.scatter(df["height"], df["age"])
    plt.title("Height vs Age")
    plt.xlabel("height")
    plt.ylabel("age")
    plt.show()

    g = df["gender"].astype("category").cat.codes

    plt.scatter(g, df["height"])
    plt.title("Gender vs Height")
    plt.xlabel("gender")
    plt.ylabel("height")
    plt.show()

    plt.scatter(g, df["weight"])
    plt.title("Gender vs Weight")
    plt.xlabel("gender")
    plt.ylabel("weight")
    plt.show()


def run():
    try:
        df = load()
        plot(df)
    except FileNotFoundError:
        print("file not found")


if __name__ == "__main__":
    run()