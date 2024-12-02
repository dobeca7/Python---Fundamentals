import re

data = input()
pattern = r'(\d+)'
while data:
    result = re.findall(pattern, data)
    if result:
        for number in result:
            print(number, end=" ")
    data = input()
