import sys

if len(sys.argv) < 2:
    print("Unesite recenicu kao argument")
    exit()
sentence = " ".join(sys.argv[1:])

uppercases = 0
lowercases = 0

for ch in sentence:
    if ch.isupper():
        uppercases = uppercases + 1
    elif ch.islower():
        lowercases = lowercases + 1

print(f"UPPER CASE {uppercases} LOWER CASE {lowercases}")