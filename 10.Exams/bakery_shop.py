bakery = {}
sold_goods = 0
while True:
    command = input().split()
    if command[0] == "Complete":
        break
    if command[0] == "Receive":
        if command[2] not in bakery:
            if int(command[1]) <= 0:
                continue
            else:
                bakery[command[2]] = 0
            bakery[command[2]] += int(command[1])
    if command[0] == "Sell":
        if command[2] not in bakery:
            print(f"You do not have any {command[2]}.")
        else:
            if int(command[1]) > bakery[command[2]]:
                del bakery[command[2]]
                print(f"There aren't enough {command[2]}. You sold the last {command[1]} of them.")
                sold_goods += int(command[1])

            if int(command[1]) <= bakery[command[2]]:
                bakery[command[2]] -= int(command[1])
                print(f"You sold {command[1]} {command[2]}.")
                sold_goods += int(command[1])
                if bakery[command[2]] == 0:
                    del bakery[command[2]]

for food, quantity in bakery.items():
    print(f"{food}: {quantity}")
print(f"All sold: {sold_goods} goods")
