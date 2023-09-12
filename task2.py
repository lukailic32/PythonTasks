import sys

if len(sys.argv) < 2:
    print("Unesite recenicu kao argument")
    exit()
sentence = " ".join(sys.argv[1:])

unique_words = []
words = sentence.split()

for word in words:
    if word not in unique_words:
        unique_words.append(word)

unique_words = sorted(unique_words)
unique_words = " ".join(unique_words)
print(unique_words)