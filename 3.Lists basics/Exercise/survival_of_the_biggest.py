list_of_integers = input().split()
numbers_to_remove = int(input())
my_list = []
for number in list_of_integers:
    my_list.append(int(number))

for j in range(numbers_to_remove):
    my_list.remove(min(my_list))
print(*my_list, sep=", ")
