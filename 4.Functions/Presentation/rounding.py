def rounding(number):
    my_numbers = []

    for j in range(len(number)):
        my_numbers.append(round(float((number[j]))))

    return my_numbers


numbers = input().split()

print(rounding(numbers))
