"""
This program creates a random NumPy array,
sorts it, and reshapes it into a matrix form.
"""

import numpy as np


def make_matrix():
    numbers = np.random.randint(1, 100, 12)
    numbers.sort()
    grid = numbers.reshape(3, 4)

    print("original array:", numbers)
    print("\nreshaped matrix:")
    print(grid)


def run():
    make_matrix()


if __name__ == "__main__":
    run()