text = input()
text_list = []
for j in text:
    text_list.append(j)

text1 = ['a', 'o', 'u', 'e', 'i']

no_vowels = [char for char in text_list if char.lower() not in text1]
print("".join(no_vowels))
