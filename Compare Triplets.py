def compareTriplets(a, b):
    alice = a.split()
    bob = b.split()
    i = 0
    a_score = 0
    b_score = 0
    while i < len(alice):
        x = int(alice[i])
        n = int(bob[i])
        if x > n:
            a_score +=1
        elif n > x:
            b_score += 1
        i+=1
    print(str(a_score) + " " + str(b_score))


aliz = input()
bobz = input()
compareTriplets(aliz, bobz)


#compareTriplets("5 6 7", "3 6 10")