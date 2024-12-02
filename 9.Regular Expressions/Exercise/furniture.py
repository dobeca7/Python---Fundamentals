import re

while True:
    line = input()
    if line == "Purchase":
        break
    pattern = r">>([A-Za-z]+)<<([0-9]+\.[0-9]+)!([0-9])"
    match = re.search(pattern, line)
    if match:
        furniture, price, quantity = match.groups()
        print("Bought furniture:")
        
            print(furniture, end="")
            print(f"Total money spend:{price}*{quantity}")

