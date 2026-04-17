# list to store user inputs
num = []

def get_input():  # input function
    print("Enter integers (or q to quit) :")

    while True:
        urs_inp = input("> ")

        # exit condition
        if urs_inp.lower() == 'q':
            break

        try:
            # convert input to integer and store it
            val = int(urs_inp)
            num.append(val)
        except ValueError:
            # handle invalid input
            print("Please enter a valid integer.")

# take inputs from user
get_input()

print("\nChecking for Armstrong numbers...")

# check each number in the list
for n in num:
    digits = str(n)
    power = len(digits)

    # calculate Armstrong sum
    total = sum(int(d) ** power for d in digits)

    # check condition
    if total == n:
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is not an Armstrong number.")