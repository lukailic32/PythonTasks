def task3():
    uppers = 0
    lowers = 0
    sentence = input("Enter a sentence: ")
    for ch in sentence:
        if ch.isupper():
            uppers = uppers + 1
        elif ch.islower():
            lowers = lowers + 1

    print(f"UPPER CASE {uppers} LOWER CASE {lowers}")