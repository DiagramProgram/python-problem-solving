# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, m, n, apples, oranges):
    appleloc = list(map(int, apples.split()))
    orangeloc = list(map(int, oranges.split()))

    applesinhouse = 0
    for each in appleloc:
        if each+a in range(s, t+1):
            applesinhouse += 1
    print(applesinhouse)
    
    orangesinhouse = 0
    for each in orangeloc:
        if each+b in range(s, t+1):
            orangesinhouse += 1
    print(orangesinhouse)

s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split()) #m is num apples and n is num oranges
apples = input()
oranges = input()
countApplesAndOranges(s, t, a, b, m, n, apples, oranges)