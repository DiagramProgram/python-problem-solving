def formingMagicSquare(s):
    print(s)


s = []
for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))
formingMagicSquare(s)