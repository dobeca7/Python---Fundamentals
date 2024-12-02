cities = {}
while True:
    command1 = input().split("||")
    if command1[0] == "Sail":
        break
    town, people, gold = command1[0], command1[1], command1[2]
    cities[town] = []
    cities[town].append(int(people))
    cities[town].append(int(gold))
while True:
    command2 = input().split("=>")
    if command2[0] == "End":
        break
    if command2[0] == "Plunder":
        cities[command2[1]][0] -= int(command2[2])
        if cities[command2[1]][0] <= 0:
            del cities[command2[1]]
        cities[command2[1]][1] -= int(command2[3])
        if cities[command2[1]][1] <= 0:
            del cities[command2[1]]
        print(f"{command2[1]} plundered! {command2[3]} gold stolen, {command2[2]} citizens killed.")
    if command2[0] == "Prosper":

        if int(command2[2]) <= 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[command2[1]][1] += int(command2[2])

            print(f"{command2[2]} gold added to the city treasury. {command2[1]} now has {cities[command2[1]][1]} gold.")
if len(cities) <
print(cities)
print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
for n in cities:
    print(f"{n} -> Population: {cities[n][0]} citizens, Gold: {cities[n][1]} kg")