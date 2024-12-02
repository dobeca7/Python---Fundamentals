lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
broken_helmet = 0
broken_sword = 0
broken_shield = 0
broken_armor = 0
for current_fight in range(1, lost_fights +1):
    if current_fight % 2 == 0:
        broken_helmet += 1
    if current_fight % 3 == 0:
        broken_sword += 1
    if current_fight % 6 == 0:
        broken_shield += 1
        if broken_shield % 2 == 0:
            broken_armor += 1
armor_expenses = broken_armor * armor_price
shield_expenses = broken_shield * shield_price
helmet_expenses = broken_helmet * helmet_price
sword_expenses = broken_sword * sword_price
final_expenses = armor_expenses + shield_expenses + helmet_expenses + sword_expenses
print(f"Gladiator expenses: {final_expenses:.2f} aureus")




