import re

string = input()
my_emails = []
emails = r"(([0-9a-z\.\-\_])+@([a-z\-]+)(\.[a-z\-]+)*\b)"
valid_email = re.findall(emails, string)
for match in valid_email:
    print(match[0])
# print(valid_email.groups[0])
