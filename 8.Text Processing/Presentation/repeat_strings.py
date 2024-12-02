strings = input().split()
my_strings = []
for n in strings:
    repeated_string = n * len(n)
    my_strings.append(repeated_string)
print("".join(my_strings))

# for string in strings:
#     repeated_string = []
#     repeated_string.append(string*len(string))
#     print(repeated_string)