students = {}
while True:
    command = input().split(":")
    if len(command) < 2:
        break
    name, ID, course = command[0], command[1], command[2]
    if course not in students:
        students[course] = []
    students[course].append(f"{name} - {ID}")
searched_course = command[0].replace("_", " ")
for student in students[searched_course]:
    print(student)


# students = {}
# command = input().split(":")
# while len(command) > 1:
#     name , id, course = command[0], command[1], command[2]
#     if course not in students.keys(): #if course not in students
#         students[course] = []
#     students[course].append(f"{name} - {id}")
#     command = input().split(":")
# searched_course = command[0].replace("_", " ")
# for student in students[searched_course]:
#     print(student)
