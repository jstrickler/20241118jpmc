fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"{fruits[0] = }")
print(f"{fruits[4] = }")
fruit_len = len(fruits)
print(f"{fruit_len = }")
print(f"{fruits[21] = }")
print(f"{fruits[fruit_len - 1] = }")
print(f"{fruits[-1] = }")
print(f"{fruits[-2] = }")
print()
#   start-at:stop-before:count-by
print(fruits[1:4])
print(f"{fruits[2:7] = }")
print(f"{fruits[:5] = }")  # first 5
print(f"{fruits[-5:] = }") # last 5

person = "Taylor Swift"
print(f"{person[:6] = }")
print(f"{person[3:6] = }")
print(f"{person[::2] = }")

