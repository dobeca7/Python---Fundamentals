def price():
    if operator == "coffee":
        return 1.50 * number_of_products
    elif operator == "water":
        return 1.00 * number_of_products
    elif operator == "coke":
        return 1.40 * number_of_products
    elif operator == "snacks":
        return 2.00 * number_of_products


operator = input()
number_of_products = float(input())
x = price()
print(f"{x:.2f}")
