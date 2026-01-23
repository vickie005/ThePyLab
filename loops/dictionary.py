students = {
    "Alice": "House1", 
    "Harry": "House1", 
    "Sofia": "House1", 
    "Ron": "House2"
    }

print(students["House1"])  # prints the value associated with the key "House1"

for student in students:
    print(student, students[student], sep=":")  # prints each student with their associated house


students = [
    {"name": "Alice", "house": "House1", "patronus": "Jane"},
    {"name": "Harry", "house": "House1", "patronus": "Mat"},
    {"name": "Sofia", "house": "House1", "patronus": "Cynthia"},
    {"name": "Ron", "house": "House2", "patronus": "none"}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=": ")  # prints each student's details

