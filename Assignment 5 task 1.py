marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 91,
    "David": 88
}

name = input("Enter the student's name: ")

if name in marks:
    print(f"{name}'s marks: {marks[name]}")
else:
    print("Student not found.")
