colors = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'white', 'black', 'puce',
'pink', 'chartreuse']

c0 = []
for c in colors:
    c0.append(c.upper())
print(f"{c0 = }\n")

#     [expr for var in iterable]
c1 = [c.upper() for c in colors]
print(f"{c1 = }\n")

c2 = [c.upper() for c in colors if c.startswith('p') if len(c) > 4]
print(f"{c2 = }\n")

c2 = []
for c in colors:
    if c.startswith('p'):
        if len(c) > 4:
            c2.append(c.upper())

c3 = [c for c in colors if c.startswith('p')]
print(f"{c3 = }\n")

c4 =  [c.upper() if c.startswith('p') else c for c in colors]
print(f"{c4 = }\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [p[-1] for p in people if p[-1] > '1970']
print(f"{dobs = }\n")

dobs = [p[-1] for p in people if p[-1].split('-')[1] == '08']
print(f"{dobs = }\n")

dobs_iter = (p[-1] for p in people)
print(f"{dobs_iter = }\n")
for dob in dobs_iter:
    print(f"{dob = }")
