n = int(input())
for j in range(1, n+1):
    digits = j
    sum_of_digits = 0
    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits/10)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{j} -> True")
    else:
        print(f"{j} -> False")










