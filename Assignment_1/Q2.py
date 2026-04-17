# Get two integer inputs from the user

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Perform the operations
addition = num1 + num2
multiplication = num1 * num2
division = num1 / num2          # Regular division (float result)
modulus = num1 % num2           # Remainder
exponentiation = num1 ** num2   # num1 raised to the power of num2

# Display results in a clean format
print("\n" + "="*60)
print("RESULTS OF OPERATIONS")
print("="*60)
print(f"Addition          : {num1} + {num2} = {addition}")
print(f"Multiplication    : {num1} * {num2} = {multiplication}")
print(f"Division          : {num1} / {num2} = {division:.4f}")
print(f"Modulus (Remainder): {num1} % {num2} = {modulus}")
print(f"Exponentiation    : {num1} ** {num2} = {exponentiation}")
print("="*60)