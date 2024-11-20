things: list[int|float] = []
things.append("abc")

cities: list[str] = [] # empty list
cities = list()  # empty list
cities = ['Portland', 'Pittsburg', 'Peoria']
print(f"cities: {cities}\n")

cities.append('Miami')
cities.append('Montgomery')
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)
print(f"cities: {cities}\n")

#   LIST.append(obj)   LIST.insert(pos, obj)  LIST.extend(iterable)

del cities[3]

print(f"cities: {cities}\n")

cities.remove('Buffalo')
print(f"cities: {cities}\n")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)
print(f"city: {city}")
print(f"cities: {cities}\n")

# del cities[x]
# del cities     remove contents and the name 'cities'
# cities.clear() remove contents only



