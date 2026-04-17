# Function to remove duplicates and sort a list
def remove_duplicates_sort(lst):
    unique_list = list(set(lst))  # remove duplicate values
    unique_list.sort()            # sort in ascending order
    return unique_list

# take input from user (space-separated numbers)
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]  # convert input strings to integers

# call function to process list
result = remove_duplicates_sort(numbers)

# display final result
print("List after removing duplicates and sorting:", result)