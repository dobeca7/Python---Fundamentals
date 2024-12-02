import re
data = input()
valid_name = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
result = re.finditer(valid_name, data)
for match in result:
    print(match.group(), end=" ")