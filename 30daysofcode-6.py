# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

for i in range(0, n):
    x = input()
    p = list(x)
    #print(p)
    even = ""
    odd = ""
    s = 0
    while s < len(p):
        if s % 2 == 0:
            even += p[s]
        else:
            odd += p[s]
        s+=1
    
    '''for each in p:
        print(each)
        print(p.index(each))
        if p.index(each) % 2 == 0:
            even += each
        else:
            odd += each'''
    
    print(even + " " + odd)
