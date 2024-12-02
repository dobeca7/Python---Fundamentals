number_of_numbers = int(input())
count_of_positives = 0
sum_of_negatives = 0
my_list_1 = []
my_list_2 = []
for n in range(number_of_numbers):
    number = int(input())
    if number > 0:
        my_list_1.append(number)
        count_of_positives += 1
    else:
        my_list_2.append(number)
        sum_of_negatives += number
print(my_list_1)
print(my_list_2)
print(f"Count of positives: {count_of_positives}")
print(f"Sum of negatives: {sum_of_negatives}")
