"""
this program defines a learner class
it stores basic details of a learner
user inputs all required attributes
an object is created using those inputs
finally it displays the learner details
"""

class Learner:
    """
    class to represent a learner with basic information
    """

    def __init__(self, student_roll, student_name, student_address, student_year, student_program, student_group):
        """
        initialize learner attributes
        """
        self.student_roll = student_roll
        self.student_name = student_name
        self.student_address = student_address
        self.student_year = student_year
        self.student_program = student_program
        self.student_group = student_group

    def show_details(self):
        """
        display learner details in a formatted way
        """
        print("\nlearner details")
        print("-" * 30)
        print(f"roll no: {self.student_roll}")
        print(f"full name: {self.student_name}")
        print(f"address: {self.student_address}")
        print(f"enrollment year: {self.student_year}")
        print(f"program: {self.student_program}")
        print(f"group: {self.student_group}")


# take input from user
roll_input = input("enter roll number: ")
name_input = input("enter full name: ")
address_input = input("enter address: ")
year_input = input("enter enrollment year: ")
program_input = input("enter program: ")
group_input = input("enter group: ")

# create learner object
learner_data = Learner(
    roll_input,
    name_input,
    address_input,
    year_input,
    program_input,
    group_input
)

# display details
learner_data.show_details()