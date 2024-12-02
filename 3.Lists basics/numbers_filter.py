n = int(input())
command_even = "even"
command_odd = "odd"
command_negative = "negative"
command_positive = "positive"
numbers = []
for j in range(n):
    number = int(input())
    numbers.append(number)
command = input()
filtered_list = []
for num in numbers:
    filtered_passes = (
        (command == command_even and num % 2 == 0) or
        (command == command_odd and num % 2 != 0) or
        (command == command_positive and num >= 0) or
        (command == command_negative and num < 0)
    )
    if filtered_passes:
        filtered_list.append(num)
print(filtered_list)








