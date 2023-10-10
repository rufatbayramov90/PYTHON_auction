students ={
    "Hanry": 81,
    "Alvera" : 75,
    "Cohn" : 99,
    "Jony" : 52
}
student_grades = {}

for stud in students:
    score = students[stud]
    if score > 80:
        student_grades[stud] = "You Passed the Exam Successfully"
    elif score > 70:
        student_grades[stud] = "You passed the exam with a few points"
    elif score > 60:
        student_grades[stud] = "Try yourself in the next exam"
    else:
        student_grades[stud] = "You failed the exam"
print(student_grades)
    


