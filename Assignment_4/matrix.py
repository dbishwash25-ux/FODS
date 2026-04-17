"""
This program performs matrix operations
and checks compatibility before calculations.
"""

import numpy as np


def get_matrix(rows, cols):
    return np.array([list(map(int, input().split())) for _ in range(rows)])


def operate(a, b, r1, c1, r2, c2):
    # addition and subtraction
    if a.shape == b.shape:
        print("\naddition:\n", a + b)
        print("\nsubtraction:\n", a - b)
    else:
        print("matrices not same size for addition or subtraction")

    # multiplication
    if c1 == r2:
        print("\nmultiplication:\n", np.dot(a, b))
    else:
        print("matrices not compatible for multiplication")


def run():
    try:
        r1 = int(input("rows matrix 1: "))
        c1 = int(input("cols matrix 1: "))
        print("enter values:")
        m1 = get_matrix(r1, c1)

        r2 = int(input("rows matrix 2: "))
        c2 = int(input("cols matrix 2: "))
        print("enter values:")
        m2 = get_matrix(r2, c2)

        operate(m1, m2, r1, c1, r2, c2)

    except Exception as e:
        print("error:", e)


if __name__ == "__main__":
     run()