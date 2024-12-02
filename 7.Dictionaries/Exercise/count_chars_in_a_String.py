characters = {}
string = input().split()
joined_string = ''.join(string)
for char in joined_string:
    if char not in characters:
        characters[char] = 0
    characters[char] += 1
for char in characters:
    print(f"{char} -> {characters[char]}")

