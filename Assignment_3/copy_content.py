"""
This program transfers text from one file into another file.
The user provides source and destination file names.
It uses exception handling to manage possible errors.
A message appears if the source file is missing.
A warning is also shown if the destination file already exists.
"""

# take filenames from user
source_file = input("Enter input file name: ")
destination_file = input("Enter output file name: ")

try:
    # open source file in read mode
    with open(source_file, "r") as read_file:
        file_content = read_file.read()

    # create destination file only if it does not exist
    try:
        with open(destination_file, "x") as write_file:
            # copy content into new file
            write_file.write(file_content)

        print("File copied successfully.")

    except FileExistsError:
        print("Output file already exists.")

except FileNotFoundError:
    print("Input file does not exist.")