line = int(input("line: "))
for i in range(1, line + 1):
    for j in range(i):
        print("*", end = '')
    print()