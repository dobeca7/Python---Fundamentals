sequence_of_numbers = input().split(" ")
my_list = []
for j in sequence_of_numbers:
    my_list.append(j)
numbers_list = list(map(int, my_list))
my_list1 = []
for k in numbers_list:
    if int(k) % 2 == 0:
        my_list1.append(k)
print(my_list1)


# def check_even(number):
#     if number % 2 == 0:
#         return True
#
#
# sequence_of_numbers = input().split(" ")
# my_list = list(map(int, sequence_of_numbers))
#
# filtered_numbers = filter(None, my_list)
# print(filtered_numbers)
# # print(check_even(my_list))
# #
# # even_numbers_iterator = filter(check_even, sequence_of_numbers))
# # even_numbers = even_numbers_iterator
# #
# print(even_numbers)
