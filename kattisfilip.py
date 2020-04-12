def filip(x, y):
    x = list(str(x))
    y = list(str(y))
    y.reverse()
    x.reverse()
    yr = list(map(int, y))
    xr = list(map(int, x))
    s = [str(i) for i in xr] 
    p = [str(i) for i in yr] 
    xfin = int("".join(s))
    yfin = int("".join(p))
    
    if xfin > yfin:
        print(xfin)
    else:
        print(yfin)



x, y = map(int, input().split())
filip(x, y)