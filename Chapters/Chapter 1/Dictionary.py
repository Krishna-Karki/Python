# marks = {
#     "krishna":100,
#     "karan":99,
#     "sewak":98,
#     97:"Ashim"
# }
# print(marks["krishna"])
# print(marks.items())
# print(marks.keys())
# marks.update({"sewak":96})
# print(marks)

# Example of a Python dictionary
student_info = {
    "name": "John Doe",
    "age": 21,
    "major": "Computer Science",
    "grades": {
        "Math": "A",
        "Physics": "B+",
        "Chemistry": "A-"
    },
    "graduated": False,
    "hobbies": ["reading", "gaming", "coding"]
}

# Accessing elements from the dictionary
print(student_info["name"])        # Output: John Doe
print(student_info["grades"]["Math"])  # Output: A
print(student_info["hobbies"])     # Output: ['reading', 'gaming', 'coding']
