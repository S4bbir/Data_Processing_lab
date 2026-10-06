def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    return average, grade


marks = [85, 78, 92, 88, 76]

average, grade = calculate_grade(marks)

print(f"Marks: {marks}")
print(f"Average Marks: {average}")
print(f"Grade: {grade}")
