# Input section: take marks of 6 subjects from the user
marks = []

for i in range(6):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

# Calculation section: compute total, average, and percentage
total = sum(marks)
average = total / 6
percentage = (total / 600) * 100

# Grade evaluation based on percentage
if percentage >= 85:
    grade = "Distinction"
elif percentage >= 70:
    grade = "First Division"
elif percentage >= 55:
    grade = "Second Division"
elif percentage >= 45:
    grade = "Third Division"
else:
    grade = "Fail"

# Output section: display results
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")