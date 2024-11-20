colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black',
'pink', 'chartreuse']

for color in colors:
    print(color)
print()

enum_colors = enumerate(colors)
print(f"{enum_colors = }")
for i, color in enum_colors:
    print(i, color)
print()
print(list(enumerate(colors)), "\n")

# reversed(LIST)  # returns iterator but does not modify list
# LIST.reverse()  # modifies list in place

print(f"{colors = }")
for color in reversed(colors):
    print(color)
print()
colors.reverse()
print(f"{colors = }")
print('-' * 60)

for i in range(5):
    print(i)
print()
print(f"{range(5) = }")
print(f"{list(range(5)) = }")
# range(start-at, stop-before, count-by)

for i in range(1, 11):
    print(i)
print()

