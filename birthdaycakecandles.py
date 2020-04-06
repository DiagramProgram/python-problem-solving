def birthdayCakeCandles(n, a):
    x = a.split()
    p = []
    for each in x:
        p.append(int(each))
    
    print(p.count(max(p)))



n = int(input())
a = input()
birthdayCakeCandles(n, a)