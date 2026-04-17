# Menu-driven program: find numbers divisible by 9 but not by 6

# User selects operation mode
a = int(input("Press 1 for default range\n"
              "Press 2 to enter custom range (1000–2500)\n"
              "\nChoose: "))

# List to store matching numbers
num = []

# Option 1: default range 1000 to 2500
if a == 1:
    for i in range(1000, 2501):
        if i % 9 == 0 and i % 6 != 0:
            num.append(i)

    print("Numbers between 1000–2500 divisible by 9 but not by 6:")
    print(num)

# Option 2: custom range input by user
elif a == 2:
    # input format: start-end
    start, end = map(int, input("Enter range (start-end): ").split("-"))

    for j in range(start, end + 1):
        if j % 9 == 0 and j % 6 != 0:
            num.append(j)

    print(f"Numbers between {start} and {end} divisible by 9 but not by 6:")
    print(num)

# Invalid menu choice
else:
    print("Invalid choice")
    exit()