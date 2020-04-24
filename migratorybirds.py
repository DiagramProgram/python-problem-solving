#I did this with a slightly more complex approach instead of creating variables of count 1-5 for increased flexibility (for fun)
def migratoryBirds(arr):
    lst = []
    i = 1
    while i < 6:
        lst.append(arr.count(i))
        i += 1
    #print(lst)
    
    locay = [i for i, x in enumerate(lst) if x == max(lst)]
    #print(locay)

    if len(locay) == 1:
        print(locay[0]+1)
    else:
        m = min(locay)
        print(m+1)


arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
migratoryBirds(arr)
