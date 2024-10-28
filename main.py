# import json
# with open('data.json', 'r') as file:
#     students = json.load(file)
# for student in students:
#     print(f"Name: {student['name']}, Age: {student['age']}")
#
# import json
# with open('students.json', 'r') as file:
#     students = json.load(file)
# new_student = {"name": "Tom", "age": 13}
# students.append(new_student)
# with open('students.json', 'w') as file:
#     json.dump(students, file)
#
# with open('tasks.txt', 'w') as file:
#     file.write('1. Finish homework\n')
#     file.write('2. Clean the room\n')
#     file.write('3. Read a book\n')
# with open('tasks.txt', 'r') as file:
#     tasks = file.read()
#     print(tasks)
#
# with open('books.txt', 'r') as file:
#     books = file.readlines()
# book_name = input("Qaysi kitobni qidiryapsiz? ")
# for book in books:
#     name, author = book.split(", ")
#     if book_name.lower() in name.lower():
#         print(f"Book: {name}, Author: {author}")
#         break
# else:
#     print("Kitob topilmadi.")

import json
with open('grades.json', 'r') as file:
    students = json.load(file)
for student in students:
    avg_grade = sum(student['grades']) / len(student['grades'])
    print(f"Name: {student['name']}, Average Grade: {avg_grade}")
