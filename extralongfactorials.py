n = int(input())

def extraLongFactorials(n):
    totfac = 1
    while n > 0:
        totfac *= n
        n-=1
    print(totfac)

extraLongFactorials(n)