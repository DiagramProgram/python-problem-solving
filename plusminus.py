def plusMinus(n, b):
    lst = b.split()
    intlst = []
    for each in lst:
        intlst.append(int(each))
    
    poscount = 0
    negcount = 0
    zerocount = 0

    for everysingle in intlst:
        if everysingle > 0:
            poscount += 1
        elif everysingle < 0:
            negcount += 1
        else:
           zerocount += 1
    
    pos = poscount/len(intlst)
    neg = negcount/len(intlst)
    zer = zerocount/len(intlst)

    print(format(pos, '.6f'))
    print(format(neg, '.6f'))
    print(format(zer, '.6f'))


n = int(input())
b = input()

plusMinus(n, b)