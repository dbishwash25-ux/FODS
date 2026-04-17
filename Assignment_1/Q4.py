# Input section: taking a number from the user
a = int(input("Enter a number: "))  # user provides the value

# Basic power calculations
print(f"The cube of {a} is", a**3)
print(f"The cube root of {a} is", round(a ** (1/3), 10))
print(f"The {a} raised to the power of six is", a**6)

# Natural logarithm calculation using series approximation
# ln(x) ≈ 2 * [(x-1)/(x+1) + (1/3)*((x-1)/(x+1))^3 + (1/5)*((x-1)/(x+1))^5]
x = (a - 1) / (a + 1)
ln = 2 * (x + (x**3)/3 + (x**5)/5)
print(f"The natural logarithm of {a} is", ln)

# Base-2 logarithm calculation using change of base formula
# log2(a) = ln(a) / ln(2)
x2 = (2 - 1) / (2 + 1)
ln2 = 2 * (x2 + (x2**3)/3 + (x2**5)/5)
log2 = ln / ln2
print(f"The Base-2 logarithm of {a} is", log2)