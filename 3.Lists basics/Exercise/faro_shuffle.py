cards = input().split()
number_of_shuffles = int(input())
for shuffle in range(number_of_shuffles):
    deck = []
    middle_of_the_deck = len(cards) // 2
    left_part_deck = cards[0: middle_of_the_deck]
    right_part_deck = cards[middle_of_the_deck: len(cards)]
    for card_index in range(len(left_part_deck)):
        deck.append(left_part_deck[card_index])
        deck.append(right_part_deck[card_index])
        cards = deck
print(deck)


