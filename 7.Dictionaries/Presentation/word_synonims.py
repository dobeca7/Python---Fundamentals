synonyms = {}
count_of_the_words = int(input())
for i in range(count_of_the_words):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)
for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")

