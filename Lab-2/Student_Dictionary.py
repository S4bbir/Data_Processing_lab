student = {
    "Name": "Sabbir",
    "ID": "24-12345-1",
    "Department": "CSE",
    "CGPA": 3.50
    }


print("Student Information:")

for key, value in student.items():
    print(f"{key} : {value}")

if student["CGPA"] >= 2.50:
    print(f"\nGood Standing")
else:
    print(f"\nAcademic Warning")