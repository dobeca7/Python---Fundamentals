def characters(char1, char2):
    my_characters = []
    for char in range(ord(char1) + 1, ord(char2)):
        my_characters.append(chr(char))

    return my_characters

character1 = input()
character2 = input()
print(' '.join(characters(character1, character2)))
