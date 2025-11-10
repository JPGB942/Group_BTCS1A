grade1 =  {
                'name'  : 'Jio Balatbat',
                'course_code' : 'APPDAET',
                'grade' : 98
          }

print(grade1['name'])
print(grade1['grade'])
print(grade1)

student_grades = [
    {'name'  : 'Jio', 'course_code' : 'APPDAET', 'grade' : 98},
    {'name'  : 'JC', 'course_code' : 'APPDAET', 'grade' : 99},
    {'name'  : 'Izo', 'course_code' : 'APPDAET', 'grade' : 100},
]

for student in student_grades:
    print(f'Name: {student["name"]}')
    print(f'Course: {student["course_code"]}')
    print(f'Grade: {student["grade"]}')