n = int(input())
word = input()
my_list = []
my_list_1 = []
for j in range(n):
    data = input()
    my_list.append(data)
    if word in data:
        my_list_1.append(data)
print(my_list)
print(my_list_1)
