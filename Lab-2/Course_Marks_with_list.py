course_mark = [75, 85, 90, 95, 46]

total_marks = sum(course_mark)
number_of_courses = len(course_mark)
average_mark = total_marks / number_of_courses
highest_mark = max(course_mark)
lowest_mark = min(course_mark)

print(f"---Course Marks Details---")
print(f"Total Marks: {total_marks}")
print(f"Average Mark: {average_mark}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")

print(f"Number Passed of Course: {len([mark for mark in course_mark if mark >= 50])} out of {number_of_courses}")
print(f"Number Failed of Course: {len([mark for mark in course_mark if mark < 50])} out of {number_of_courses}")

print(f"\n \n---Course Marks Details With user input---")
course_marks = []
for i in range(5):
    mark = int(input(f"Enter mark for course {i + 1}: "))
    course_marks.append(mark)

total_marks = sum(course_marks)
number_of_courses = len(course_marks)
average_mark = total_marks / number_of_courses
highest_mark = max(course_marks)
lowest_mark = min(course_marks)

print(f"\nCourse Marks: {course_marks}")
print(f"Total Marks: {total_marks}")
print(f"Average Mark: {average_mark}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")

print(f"Number Passed of Course: {len([mark for mark in course_marks if mark >= 50])} out of {number_of_courses}")
print(f"Number Failed of Course: {len([mark for mark in course_marks if mark < 50])} out of {number_of_courses}")