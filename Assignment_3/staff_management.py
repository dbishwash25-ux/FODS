"""
this program defines a staff class to store staff details
it allows user to add multiple staff records
data is saved into a csv file
it uses try except to handle file errors
user can also view all saved staff records
"""

import csv


class Staff:
    """
    class to represent a staff member
    """

    def __init__(self, emp_id, full_name, address, phone_number, marital_status, dependents, salary):
        """
        initialize staff attributes
        """
        self.emp_id = emp_id
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.marital_status = marital_status
        self.dependents = dependents
        self.salary = salary

    def get_record(self):
        """
        convert object data into list
        """
        return [
            self.emp_id,
            self.full_name,
            self.address,
            self.phone_number,
            self.marital_status,
            self.dependents,
            self.salary
        ]


csv_file = "staff.csv"


# function to insert staff data
def save_staff():
    try:
        # take input
        id_input = input("enter employee id: ")
        name_input = input("enter full name: ")
        address_input = input("enter address: ")
        phone_input = input("enter phone number: ")
        status_input = input("enter marital status: ")
        dependent_input = input("enter dependents: ")
        salary_input = input("enter salary: ")

        # create object
        staff_data = Staff(
            id_input,
            name_input,
            address_input,
            phone_input,
            status_input,
            dependent_input,
            salary_input
        )

        # write into csv file
        with open(csv_file, "a", newline="") as file_data:
            csv_writer = csv.writer(file_data)
            csv_writer.writerow(staff_data.get_record())

        print("staff record saved successfully")

    except Exception:
        print("error while saving staff data")


# function to display staff data
def show_staff():
    try:
        with open(csv_file, "r") as file_data:
            csv_reader = csv.reader(file_data)

            print("\nstaff records")
            print("=" * 60)

            for row_data in csv_reader:
                print(f"employee id: {row_data[0]}")
                print(f"full name: {row_data[1]}")
                print(f"address: {row_data[2]}")
                print(f"phone number: {row_data[3]}")
                print(f"marital status: {row_data[4]}")
                print(f"dependents: {row_data[5]}")
                print(f"salary: {row_data[6]}")
                print("-" * 60)

    except FileNotFoundError:
        print("staff file not found")

    except Exception:
        print("error while reading file")


# main menu
while True:
    print("\n1. add staff")
    print("2. view staff")
    print("3. exit")

    user_choice = input("enter choice: ")

    if user_choice == "1":
        save_staff()

    elif user_choice == "2":
        show_staff()

    elif user_choice == "3":
        print("program closed")
        break

    else:
        print("invalid choice")