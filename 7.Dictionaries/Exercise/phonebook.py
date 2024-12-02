phonebook = {}

while True:
    name_and_number = input()
    if "-" not in name_and_number:
        break
    name, phone = name_and_number.split("-")
    phonebook[name] = phone

for check in range(int(name_and_number)):
    contacts = input()
    if contacts not in phonebook.keys():
        print(f"Contact {contacts} does not exist.")
    else:
        print(f"{contacts} -> {phonebook[contacts]}")

    # for data in range(0, len(name_and_number))
    #     key = name_and_number[data]
    #     value = name_and_number[data + 1]
    #     phonebook[key] = value
    # print(phonebook)