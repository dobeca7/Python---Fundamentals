import re

string = ""
while True:
    command = input().split()
    if command[0] == "End":
        break
    if command[0] == "Add":
        string = string + command[1]
    if command[0] == "Upgrade":
        for char in string:
            if char == command[1]:
                string = string.replace(char, chr(ord(char) + 1))
    if command[0] == "Print":
        print(string)
    if command[0] == "Index":
        if command[1] not in string:
            print("None")
        else:
            indexes = [i for i, c in enumerate(string) if c == command[1]]
            my_list = []
            for index in indexes:
                my_list.append(str(index))
            print(" ".join(my_list))

    if command[0] == "Remove":
        if command[1] in string:
            string = string.replace(command[1], "")
