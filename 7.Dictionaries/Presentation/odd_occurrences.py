words = {}
line_of_words = input().lower()
list_of_line_of_words = line_of_words.split()
for word in list_of_line_of_words:
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1
for key, value in words.items():
    if value % 2 != 0:
        print(key, end=" ")





