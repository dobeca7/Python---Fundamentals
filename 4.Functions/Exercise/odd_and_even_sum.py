def all_even_all_odd(number):
    sum_of_even_digits = 0
    sum_of_odd_digits = 0
    for digit in number:
        if int(digit) % 2 == 0:
            sum_of_odd_digits += int(digit)
        if int(digit) % 2 != 0:
            sum_of_even_digits += int(digit)
    return sum_of_even_digits, sum_of_odd_digits


single_number = input()
sum_of_odd_digits, sum_of_even_digits = all_even_all_odd(single_number)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
