def simpleArraySum(a, b):
    nums = b.split()
    sum = 0
    for each in nums:
        sum+= int(each)
    print(sum)

n = int(input())
numberz = input()
simpleArraySum(n, numberz)


#simpleArraySum("6", "1 2 3 4 10 11")