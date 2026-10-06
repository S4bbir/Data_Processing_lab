# List of 5 students
students = [
    {"name": "Sabbir", "department": "Data Science", "marks": 85, "attendance": 90},
    {"name": "Rahim", "department": "CSE", "marks": 78, "attendance": 75},
    {"name": "Karim", "department": "EEE", "marks": 92, "attendance": 88},
    {"name": "Nabil", "department": "Data Science", "marks": 70, "attendance": 65},
    {"name": "Tanvir", "department": "CSE", "marks": 88, "attendance": 82}
]


#verage marks
def calculate_average_marks(students):
    total = 0

    for student in students:
        total = total + student["marks"]

    average = total / len(students)
    return average


#highest marks
def find_highest_marks(students):
    highest = students[0]

    for student in students:
        if student["marks"] > highest["marks"]:
            highest = student

    return highest


#attendance below 80%
def count_low_attendance(students):
    count = 0

    for student in students:
        if student["attendance"] < 80:
            count = count + 1

    return count


# Print the summary
print("--- Student Summary ---")
print(f"Average Marks {calculate_average_marks(students)}")
print(f"Highest Marks: {find_highest_marks(students)}")
print(f"Students with attendance below 80%: {count_low_attendance(students)}")