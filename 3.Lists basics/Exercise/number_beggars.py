money = input().split(", ")
money_as_digits = []
for element in money:
    money_as_digits.append(int(element))
count_of_beggars = int(input())
final_sum = []
starting_index = 0
while starting_index < count_of_beggars:
    money_per_beggar = 0
    for current_index in range(starting_index, len(money_as_digits), count_of_beggars):
        money_per_beggar += money_as_digits[current_index]
    final_sum.append(money_per_beggar)
    starting_index += 1
print(final_sum)
