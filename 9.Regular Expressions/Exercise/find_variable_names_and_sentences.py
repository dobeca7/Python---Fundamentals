import re
data = input()
pattern = r'\b_([a-zA-Z]*)\b'
result = re.findall(pattern, data)
print(",".join(result))
    # if result:
    #     for number in result:
    #         print(number, end=" ")
    # data = input()