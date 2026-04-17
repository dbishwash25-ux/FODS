"""
Program to take a list of numbers from the user,
sort it, and perform slicing operations.
"""

def get_numbers():
    # take input from user and convert to list of integers
    nums = list(map(int, input("Enter at least 12 numbers separated by space: ").split()))
    
    # ensure minimum requirement
    if len(nums) < 12:
        print("Please enter at least 12 numbers.")
        return None
    
    return nums


def process_list(nums):
    # sort the list in ascending order
    nums.sort()
    print("Sorted list:", nums)

    # slicing operations (end index is exclusive)
    print("Elements from index 3 to 6:", nums[3:7])
    print("Elements from index 6 to 9:", nums[6:10])
    print("Elements from index 4 to 10:", nums[4:11])


def main():
    nums = get_numbers()
    if nums:
        process_list(nums)


# program entry point
if __name__ == "__main__":
    main()