students = [
    {"name": "Sabbir", "department": "CSE", "marks": 85, "attendance": 90},
    {"name": "Rahim", "department": "EEE", "marks": 78, "attendance": 75},
    {"name": "Karim", "department": "CSE", "marks": 92, "attendance": 88},
    {"name": "Nadia", "department": "BBA", "marks": 69, "attendance": 70},
    {"name": "Tanvir", "department": "CSE", "marks": 81, "attendance": 82}
    ]


#calculate average marks
def calculate_average(students):
    total = 0
    for student in students:
        total += student["marks"]
    average = total / len(students)
    return average


#highest marks
def find_highest_marks(students):
    highest = 0
    for student in students:
        if student["marks"] > highest:
            highest = student["marks"]
    return highest


#lowest marks
def find_lowest_marks(students):
    lowest = 100
    for student in students:
        if student["marks"] < lowest:
            lowest = student["marks"]
    return lowest


#attendance percentage below 80
def count_low_attendance(students):
    count = 0
    for student in students:
        if student["attendance"] < 80:
            count += 1
    return count


print(f"--Student Summary--")
print(f"Avarage Marks: {calculate_average(students)}")
print(f"Highest Marks: {find_highest_marks(students)}")
print(f"Lowest Marks: {find_lowest_marks(students)}")