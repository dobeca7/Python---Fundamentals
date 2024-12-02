def palindrome_function(numbers):
    for num in numbers:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


list_of_positive_integers = input().split(", ")
my_list = list(map(str, list_of_positive_integers))
palindrome_number = palindrome_function(my_list)
