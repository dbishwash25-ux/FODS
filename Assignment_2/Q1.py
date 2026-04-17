# Function to add two numbers
def add_num(a, b):
    return a + b


# Function to find absolute difference between two numbers
def diff_num(a, b):
    if a > b:
        return a - b
    else:
        return b - a


# Function to multiply two numbers
def product_num(a, b):
    return a * b


# Function to divide two numbers safely
def quotient_num(a, b):
    # Avoid division by zero
    if a == 0 or b == 0:
        return "undefined (division by zero)"

    # Return larger divided by smaller for consistency
    if a > b:
        return a / b
    else:
        return b / a


# Input values (can be modified or taken from user)
num1 = 4
num2 = 2

# Display results of all operations
print("Sum:", add_num(num1, num2))
print("Difference:", diff_num(num1, num2))
print("Product:", product_num(num1, num2))
print("Quotient:", quotient_num(num1, num2))