import csv

def append_record():
    student_name = input("Enter Student Name: ")
    student_roll = input("Enter Roll No: ")
    student_program = input("Enter Program: ")
    student_year = input("Enter Year: ")
    student_group = input("Enter Group: ")

    field_names = ['student_name', 'roll_no', 'program', 'year', 'group']

    with open('records.csv', 'a', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=field_names)

        if file.tell() == 0:
            csv_writer.writeheader()

        csv_writer.writerow({
            'student_name': student_name,
            'roll_no': student_roll,
            'program': student_program,
            'year': student_year,
            'group': student_group
        })

    print("Record added successfully.")

if __name__ == "__main__":
    append_record()