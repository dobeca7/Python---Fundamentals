string = input()
while True:
    command = input().split(">>>")
    if command[0] == "Generate":
        print(f"Your activation key is: {string}")
        break
    if command[0] == "Contains":
        if command[1] in string:
            print(f"{string} contains {command[1]}")
        else:
            print("Substring not found!")
    if command[0] == "Flip" and command[1] == "Upper":
        string = string[0:int(command[2])] + string[int(command[2]):int(command[3])].upper() + string[int(command[3]):]
        print(string)
    if command[0] == "Flip" and command[1] == "Lower":
        string = string[0:int(command[2])] + string[int(command[2]):int(command[3])].lower() + string[int(command[3]):]
        print(string)
    if command[0] == "Slice":
        string = string[0:int(command[1])] + string[int(command[2]):]
        print(string)
