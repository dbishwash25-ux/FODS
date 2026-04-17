"""
this program creates a numpy array and performs operations
it calculates sum mean maximum and minimum values
"""

import numpy as np

def perform_operations(arr):
    # calculate values
    total_sum = np.sum(arr)
    mean_value = np.mean(arr)
    largest_value = np.max(arr)
    smallest_value = np.min(arr)

    # display results
    print("array:", arr)
    print("sum:", total_sum)
    print("mean:", mean_value)
    print("max:", largest_value)
    print("min:", smallest_value)


def main():
    arr = np.array([10, 20, 30, 40, 50])
    perform_operations(arr)


if __name__ == "__main__":
    main()