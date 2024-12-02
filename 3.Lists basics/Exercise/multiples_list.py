factor = int(input())
count = int(input())

my_list = []
for current_number in range(1, count+1):
    new_factor = factor * current_number
    my_list.append(new_factor)
print(my_list)