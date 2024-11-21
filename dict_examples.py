d1 = {}  # empty dictionary
d2 = dict() # same

d3 = {'a':9, 'm': 18, 'z': 3}

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

print(f"{airports['RDU'] = }")
print(f"{airports['YYZ'] = }")
airports['GLA'] = "Glasgow"  # add element
airports['RDU'] = 'Durham'   # overwrite element if key exists

# print(f"{airports['VCE'] = }")
print(f"{airports.get('VCE') = }")
print(f"{airports.get('VCE', 42) = }")
airports[None] = "abc"
print(f"{airports[None] = }")
print(f"{airports.setdefault('VCE', 'Venice') = }")
print(f"{airports = }\n")
print(f"{airports.setdefault('RDU', 'RALLLLLLLEIGH') = }")
print()

for code, city in airports.items():
    print(code, city)
print()
