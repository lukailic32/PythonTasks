MIN = 1000
MAX = 3000
DIVIDER = 9
NOT_DIVIDER = 5
resultList = []


for i in range(MIN, MAX+1):
    if i % DIVIDER == 0 and i % NOT_DIVIDER != 0:
        resultList.append(i)
print(", ".join(map(str, resultList)))