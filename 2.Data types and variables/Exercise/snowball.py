number_of_snowballs = int(input())
highest_value = 0
snowball_value = 0
max_weight = 0
max_time = 0
max_quality = 0
for current_snowball in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    snowball_value = (weight / time) ** quality
    if snowball_value > highest_value:
        highest_value = snowball_value
        max_weight = weight
        max_time = time
        max_quality = quality


print(f"{max_weight} : {max_time} = {int(highest_value)} ({max_quality})")


