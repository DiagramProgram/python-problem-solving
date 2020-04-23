def diagonalDifference(arr):
    d1sum, d2sum = 0, 0

    for i in range(len(arr[0])):
        d1sum += arr[i][i]

    i = 0
    while i < len(arr[0]):
        for x in range(len(arr[0])-1, -1, -1):
            d2sum += arr[i][x]
            i += 1

    print(abs(d1sum-d2sum))

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip().split())))

diagonalDifference(arr)
