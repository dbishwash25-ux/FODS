# Import random module to generate a secret number
import random

# Welcome message
print("Hi! Welcome to the Number Guessing Game")
print("You have 7 chances to guess the correct number")

# Define guessing range
low = 1
high = 50

print(f"\nGuess the number between {low} and {high}. Let's begin!")

# Generate random target number
num = random.randint(low, high)

# Total allowed attempts
ch = 7
attempts = 0

# Game loop
while attempts < ch:
    
    # Track number of attempts used
    attempts += 1

    # Take user input
    guess = int(input("Enter your guess: "))

    # Check if guess is correct
    if guess == num:
        print(f"Correct! The number was {num}. You guessed it in {attempts} attempts.")
        break

    # If last attempt is reached and guess is wrong
    elif attempts == ch:
        print(f"Sorry! The number was {num}. Better luck next time!")

    # Provide hints
    elif guess > num:
        print("Too high! Try a lower number.")
    else:
        print("Too low! Try a higher number.")