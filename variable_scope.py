COLOR = "blue"  # GLOBAL (file)

def spam():
    animal = "wombat"  # LOCAL
    print(f"{COLOR = }")
    print(f"{animal = }")
    
    def ham():
        return 100
    return ham

f = spam()
print(f"{f() = }")

# print(f"{animal = }")
