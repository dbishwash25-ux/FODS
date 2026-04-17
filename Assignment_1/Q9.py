# Menu-driven program to calculate sum of positive and negative numbers

# Variables to store cumulative sums
positive_sum = 0
negative_sum = 0

while True:
    # Display menu options
    print("\nMenu:")
    print("n - Enter a number")
    print("q - Quit")

    # Get user choice
    choice = input("Enter your choice: ")

    if choice == 'n':
        # Input a number from user
        num = float(input("Enter a number: "))

        # Add to appropriate sum based on sign
        if num > 0:
            positive_sum += num
        elif num < 0:
            negative_sum += num

    elif choice == 'q':
        # Exit the loop
        break

    else:
        print("Invalid choice! Please try again.")

# Final results display
print(f"Sum of positive numbers: {positive_sum}")
print(f"Sum of negative numbers: {negative_sum}")