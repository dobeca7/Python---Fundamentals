wagons = int(input())
train = []
for j in range(wagons):
    train.append(0)
while True:
    command = input()
    if command == "End":
        break
    split_command = command.split(' ')
    current_command = split_command[0]

    if current_command == "add":
        add_command = int(split_command[1])
        train[-1] += add_command
    if current_command == "insert":
        current_index = int(split_command[1])
        inserted_people = int(split_command[2])
        train[current_index] += inserted_people
    if current_command == "leave":
        current_index = int(split_command[1])
        people_to_leave = int(split_command[2])
        train[current_index] -= people_to_leave
print(train)


