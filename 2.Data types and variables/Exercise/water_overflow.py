water_tank = 255
number_of_lines = int(input())
capacity = 0
for j in range(number_of_lines):
    liters_of_water = int(input())
    capacity += liters_of_water
    if capacity > water_tank:
        capacity -= liters_of_water
        print("Insufficient capacity!")
        continue
print(capacity)




