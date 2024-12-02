number_of_people = int(input())
capacity = int(input())
number_of_courses = number_of_people // capacity
if number_of_people % capacity != 0:
    number_of_courses += 1
print(number_of_courses)