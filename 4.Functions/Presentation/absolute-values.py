numbers = input().split()
my_numbers = []
for num in numbers:
	my_numbers.append(abs(float(num)))
print(my_numbers)