countries = input().split(", ")
cities = input().split(", ")
# final_result = {countries[index]: cities[index] for index in range(len(countries))}
final_result = dict(zip(countries, cities))
for countries, cities in final_result.items():
    print(f"{countries} -> {cities}")