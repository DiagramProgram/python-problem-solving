def divisibleSumPairs(n, k, ar):
    num = 0
    i = 0
    while i < len(ar):
        p = 0
        while p < len(ar) and p != i:
            if (ar[i] + ar[p])%k == 0:
                num += 1
            p += 1
        i += 1
    print(num)



nk = input().split()
n = int(nk[0])
k = int(nk[1])
ar = list(map(int, input().strip().split()))
divisibleSumPairs(n, k, ar)