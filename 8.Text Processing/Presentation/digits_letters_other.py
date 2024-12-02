string = input()
digits = []
letters = []
other = []
for j in string:
    if j.isdigit():
        digits.append(j)
    elif j.isalpha():
        letters.append(j)
    else:
        other.append(j)
print("".join(digits))
print("".join(letters))
print("".join(other))

