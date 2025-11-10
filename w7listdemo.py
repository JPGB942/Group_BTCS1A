#list demo
students = ['JC', 'Izo', 'Anne', 'Rannier']
combined = ['JC', 98, 'Izo', 97, 'Anne', 99, 'Rannier']

students_grades = [
                    ['Jc', 98],
                    ['Izo', 97],
                    ['Anne', 99]
                  ]
print(students)
students.append('John')
print(students)
students.remove('John')
print(students)

print(students_grades)
#---- Long method using lists and the for loop -------
new_student = []
for student in students:
    new_student.append(f'*{student}*')

print(f"Long Method: {new_student}")

#------Short method using list comprehensions ----------
ns = [f'*{student}*' for student in students]
print(f"Short method: {ns}")

#another method of list using list comprehension
grades = [88, 86, 90, 69, 75]
marks = []
for grade in grades:
    marks.append('P' if grade >= 70 else 'F')

print(f"Long method: {marks}")

mrks = ['P' if grade <= 70 else 'F' for grade in grades]
print(f"Short method: {mrks}")

##pop quiz: using list comprehension. needs to return the number multiplied by 100
n = [4, 8, 16, 12, 10, 100]
na = [m * 100 for m in n]
print(na)

#list comprehension = print all even numbers in a sequence from 0 to 100
print([n for n in range(101) if n % 2 ==0])

# Print all numbers that are divisible by 6
print([p for p in range(101) if p % 6 == 0])

def get_gpa(grade):
    if grade >= 97: return '4.0'
    elif grade >= 93: return '3.5'
    elif grade >= 89: return '3.0'
    elif grade >= 85: return '2.5'
    elif grade >= 80: return '2.0'
    elif grade >= 75: return '1.5'
    elif grade >= 70: return '1.0'
    else: return 'R'
