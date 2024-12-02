import re
data = input()
valid_name = r'\b([0-9]{2})([\/.-])([A-Z][a-z]{2})\2([0-9]+)'
result = re.findall(valid_name, data)
for element in result:
    print(f"Day: {element[0]}, Month: {element[2]}, Year: {element[3]}")