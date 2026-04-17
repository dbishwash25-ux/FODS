
# Basic Arithmetic Functions

def add(a, b):
    """Returns the sum of two numbers"""
    return a + b


def mult(a, b):
    """Returns the product of two numbers"""
    return a * b


def div(a, b):
    """Returns normal division result, handles divide-by-zero"""
    if b == 0:
        return "Can't divide by Zero"
    return a / b


def floordiv(a, b):
    """Returns floor division result, handles divide-by-zero"""
    if b == 0:
        return "Can't divide by Zero"
    return a // b


def exp(a, b):
    """Returns a raised to the power of b"""
    return a ** b

# User Input Section

try:
    # Taking inputs from user
    num = int(input("Enter first number: "))
    num1 = int(input("Enter second number: "))

    # Output Section

    print("\n--- Results ---")
    print(f"Sum is {add(num, num1)}")
    print(f"Product is {mult(num, num1)}")
    print(f"Division is {div(num, num1)}")
    print(f"Floor Division is {floordiv(num, num1)}")
    print(f"Exponentiation is {exp(num, num1)}")

except ValueError:
    print("Please enter valid integers only!")