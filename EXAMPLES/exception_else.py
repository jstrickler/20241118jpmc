class WhoopeeError(Exception):
    pass # do nothing

numpairs = [(5, 1), (1, 5), (5, 0), (0, 5)]

total = 0

for x, y in numpairs:
    try:
        quotient = x / y
    except ZeroDivisionError as err:
        print(f"uh-oh, when y = {y}, {err}")
        raise
    except RuntimeError as err:
        print("OOPS!", err)
    else:
        total += quotient  # Only if no exceptions were raised
print(total)

def spam():
    raise WhoopeeError("Having fun now!")

try:
    spam()
except WhoopeeError as err:
    print(err)
