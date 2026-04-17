# Exception handling is used to avoid errors from invalid input
# The try block executes the main logic, while except handles wrong inputs

try:
    # Take integer input from the user
    a = int(input("Enter a number "))

    # Special case: zero handling
    # 0 is neither positive nor negative, but it is even
    if a == 0:
        print(f"This is {a}. Please enter a number other than 0")

    # Check if the number is positive
    if a > 0:
        print(f"{a} is a positive number")

    # Check if the number is even
    elif a % 2 == 0:
        print(f"{a} is even")

    # Check if the number is positive and odd
    elif a > 0 and a % 2 == 1:
        print(f"{a} is a positive odd number")

    # Check if the number is negative
    elif a < 0:
        print(f"{a} is a negative number")

    # Check if the number is negative and odd
    elif a < 0 and a % 2 == 1:
        print(f"{a} is a negative odd number")

# Handles invalid inputs such as strings or special characters
except ValueError:
    print("Invalid input. Please enter a valid number.")