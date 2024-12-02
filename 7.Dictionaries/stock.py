data = input().split()
searched_products = input().split()
bakery = {}
for element in range(0, len(data), 2):
    key = data[element]
    value = data[element + 1]
    bakery[key] = int(value)
for product in searched_products :
    if product not in bakery.keys():
        print(f"Sorry, we don't have {product}")
    else:
        quantity = bakery[product]
        print(f"We have {quantity} of {product} left")



