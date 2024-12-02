numbers = list(input().split(", "))
integers = [int(i) for i in numbers]
without_zero = []
with_zero = []
for i in integers:
    if i != 0:
        without_zero.append(i)
    else:
        with_zero.append(i)
final = without_zero+with_zero
print(final)




