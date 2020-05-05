def miniMaxSum(a):
    p = a.split()
    n = []
    s = []
    for each in p:
        n.append(int(each))
        s.append(int(each))
    #   print(n)
    
    x = []
    for i in range(4):
        biggest = max(n)
        x.append(biggest)
        #print(x)
        n.remove(biggest)

    totmax = 0
    for each in x:
        totmax += each

    y = []
    for i in range(4):
        smallest = min(s)
        y.append(smallest)
        #print(y)
        s.remove(smallest)

    totmin = 0
    for each in y:
        totmin += each
    print(str(totmin) + " " + str(totmax))


a = input()
miniMaxSum(a)