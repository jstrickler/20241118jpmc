
set1 = {'red', 'blue', 'green', 'purple', 'green'}  # create literal set
set2 = {'green', 'blue', 'yellow', 'orange'}

# s = set(ITERABLE)
# s = set()  empty set
# s.add(x)
# s.add(y)

set1.add('taupe')  # add element to set (ignored if already in set)

print(f"{set1 = }")
print(f"{set2 = }")
print(f"{set1 & set2 = }")  # intersection -- common items
print(f"{set1 ^ set2 = }")  # XOR -- non-common items (in one set but not both)
print(f"{set1 | set2 = }")  # union -- unique combination of both sets
print(f"{set1 - set2 = }")  # difference -- Remove items in right set from left set
print(f"{set2 - set1 = }")
print()

with open('../DATA/breakfast.txt') as breakfast_in:
    food = breakfast_in.read().splitlines()

print(f"{food = }")

unique_food = set(food)  # Create set from iterable (e.g., list)
print(f"{unique_food = }")
