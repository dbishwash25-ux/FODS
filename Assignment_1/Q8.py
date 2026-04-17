# Program to calculate factorial of a number

# Instruction for the user
print("Note: The number should be positive")

# Input section: take number from user
n = int(input("Enter the number whose factorial you want: "))

# List to store numbers used in factorial calculation
num = []

# Variable to store factorial result
output = 1

# Check if input is valid (non-negative)
if n >= 0:

    # Loop to calculate factorial and store values
    for i in range(1, n + 1):
        output *= i
        num.append(i)

    # Display intermediate numbers used
    print("Numbers used in calculation:", num)

    # Display final result
    print(f"Factorial of {n} is", output)

# Handle negative input
else:
    print("Invalid input. Please enter a positive integer")