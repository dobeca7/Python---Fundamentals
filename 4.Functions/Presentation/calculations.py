def calculator(num_1, num_2, operator):
    if operator == "multiply":
        return num_1 * num_2
    if operator == "divide":
        return num_1 / num_2
    if operator == "add":
        return num_1 + num_2
    if operator == "subtract":
        return num_1 - num_2


operation = input()
first_number = int(input())
second_number = int(input())
print(calculator(first_number, second_number, operation))
