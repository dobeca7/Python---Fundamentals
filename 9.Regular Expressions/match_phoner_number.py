import re
data = input()
valid_name = r'\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b'
result = re.findall(valid_name, data)
print(", ".join(result))