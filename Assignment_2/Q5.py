def reverse_sort(names):
    return sorted (names, reverse=True)

student_lst = []
students = input("Enter the name of students and seperate each names by space: ").split()
student_lst.append(students)

print("The orignal list: ",students)
print("\nThe reverse sorted list: ")
print(reverse_sort(students))