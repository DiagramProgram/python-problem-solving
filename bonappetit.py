def bonAppetit(bill, k, b):
    i = 0
    #print(bill)
    annasum = 0
    while i < n:
        annasum += bill[i]
        i+=1
    #print(annasum)
    
    annasum = annasum - bill[k]
    annasum = annasum//2
    if b == annasum:
        print("Bon Appetit")
    else:
        print(b-annasum)


n, k = map(int, input().split()) #num items ordered and 0-base index of item anna doesnt eat
bill = list(map(int, input().rstrip().split()))
b = int(input())

bonAppetit(bill, k, b)