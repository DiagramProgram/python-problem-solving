def soundsfishy(a, b, c, d):
    
    if a < b < c < d:
        print("Fish Rising")
    elif a > b > c > d:
        print("Fish Diving")
    elif a == b == c == d:
        print("Fish At Constant Depth")
    else:
        print("No Fish")

a = int(input())
b = int(input())
c = int(input())
d = int(input())

soundsfishy(a, b, c, d)