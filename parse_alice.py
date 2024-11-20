import sys

start_letter = sys.argv[1]

for file_path in sys.argv[2:]:

    count = 0
    with open(file_path) as alice_in:
        for raw_line in alice_in:
            if raw_line.startswith(start_letter):
                count += 1

    print(f"{count} lines in {file_path} start with '{start_letter}'")