# Complete the countingValleys function below.
def countingValleys(n, s):
    a = list(s)
    x = []
    for each in a:
        if each == "U":
            x.append(1)
        else:
            x.append(-1)
    #print(x)
    p = 0
    y = 0
    l = 0
    #print(len(x))
    while y < len(x):
        p += x[y]
        #print(p)
        if p == 0 and x[y] == 1:
            l += 1
        y += 1

    '''for y in x:
        p += y
        if p == 0 and y == 1:
            l += 1
        #y += 1'''
    
    print(l)


n = int(input())
steps = input()
countingValleys(n, steps)
