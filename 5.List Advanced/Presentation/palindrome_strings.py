words = input().split(" ")
palindrome = input()
palindrome_counter = 0
palindrome_words = [word for word in words if word == word[::-1]]
for n in palindrome_words:
    if n == palindrome:
        palindrome_counter += 1
print(palindrome_words)
print(f"Found palindrome {palindrome_counter} times")

