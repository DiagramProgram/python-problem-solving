def breakingRecords(n, scores):
    max = scores[0]
    min = scores[0]
    maxnum = 0
    minnum = 0
    for each in scores:
        if each > max:
            max = each
            maxnum +=1
        elif each < min:
            min = each
            minnum += 1
    print(str(maxnum) + " " + str(minnum))


n = int(input())
scores = list(map(int, input().rstrip().split()))
breakingRecords(n, scores)