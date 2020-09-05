students = {
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}

def get_student_names(students):
    return sorted(students.values())

print(get_student_names(students))
    