def perfect_number(num):
    perfection = True
    my_list = []
    for n in range(1, num):
        if num % n == 0:
            my_list.append(n)
    sum_counter = 0
    for j in my_list:
        sum_counter += j
    if sum_counter == num:
        return perfection
    



number = int(input())
the_perfect_number = perfect_number(number)
if the_perfect_number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

