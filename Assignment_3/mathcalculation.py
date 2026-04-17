"""
This application accepts multiple whole numbers from the user.
It calculates sum, difference, product, and quotient values.
Each result is stored in a file along with the current timestamp.
The program continues until the user enters exit.
When finished, all stored records are displayed neatly.
"""

import datetime

# filename used for storing output records
result_file = "math_results.txt"

# open file in append mode
data_file = open(result_file, "a")

while True:
    # accept numbers from user
    user_input = input("Enter integers separated by space or type exit: ")

    # stop program if user types exit
    if user_input.lower() == "exit":
        break

    # convert entered values into integer list
    try:
        number_values = list(map(int, user_input.split()))
    except:
        print("Invalid input, try again.")
        continue

    # ensure minimum two numbers are entered
    if len(number_values) < 2:
        print("Enter at least two numbers.")
        continue

    # calculate addition
    total_sum = sum(number_values)

    # calculate subtraction
    total_difference = number_values[0]
    for value in number_values[1:]:
        total_difference -= value

    # calculate multiplication
    total_product = 1
    for value in number_values:
        total_product *= value

    # calculate division
    total_quotient = number_values[0]
    try:
        for value in number_values[1:]:
            total_quotient /= value
    except ZeroDivisionError:
        total_quotient = "undefined"

    # current date and time
    current_time = datetime.datetime.now()

    # save results into file
    data_file.write(f"\n{current_time}\n")
    data_file.write(f"numbers: {number_values}\n")
    data_file.write(f"addition: {total_sum}\n")
    data_file.write(f"subtraction: {total_difference}\n")
    data_file.write(f"multiplication: {total_product}\n")
    data_file.write(f"division: {total_quotient}\n")
    data_file.write("*" * 35 + "\n")

# close file
data_file.close()

# display saved content
print("\nSaved Results\n")
print("=" * 35)

with open(result_file, "r") as read_file:
    print(read_file.read())