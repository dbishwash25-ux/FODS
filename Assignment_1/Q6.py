# Function to check whether a number is prime
def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False

    # Check divisibility up to square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Input section: take range from user
start = int(input("Enter starting value of range: "))
end = int(input("Enter ending value of range: "))

# Generate list of prime numbers in the given range
primes = []
for num in range(start, end + 1):
    if is_prime(num):
        primes.append(num)

# Output results
print(f"\nPrime numbers between {start} and {end}: {primes}")
print(f"Total prime count: {len(primes)}")
print(f"Sum of primes: {sum(primes)}")