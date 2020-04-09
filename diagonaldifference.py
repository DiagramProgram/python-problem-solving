n = int(input())

def diagonalDifference(n):
    biglist = []
    for i in range(n):
        x = input()
        s = x.split()
        biglist += s
    #print(biglist)

    intlist = []
    for each in biglist:
        x = int(each)
        intlist.append(x)
    #print(intlist)
    
    rightdiag = 0
    o = 0
    while o < len(intlist):
        rightdiag += intlist[o]
        o += n+1
    #print(rightdiag)

    leftdiag = 0
    p = n-1
    #len(intlist) is 9
    while p < len(intlist)-n+1:
        leftdiag += intlist[p]
        p += n-1
    #print(leftdiag)
    
    if rightdiag > leftdiag:
        print(rightdiag-leftdiag)
    elif leftdiag > rightdiag:
        print(leftdiag-rightdiag)
    else:
        print(0)

diagonalDifference(n)