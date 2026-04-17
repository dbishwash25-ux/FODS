import csv 
def read_info():
    try:
        with open('records.csv','r', newline='' ) as file:
            filereader = csv.DictReader(file, skipinitialspace=True)
            print(f"{'Name':<15} {'Roll':<10} {'Program':<20} {'Year':<10} {'Group'}")
            print("=" * 66)
            for row in filereader:
                print(f"{row['student_name']:<15} {row['roll_no']:<10} {row['program']:<20} {row['year']:<10} {row['group']}")
    except FileNotFoundError:
        print("File not visible")
if __name__=="__main__":
    read_info()