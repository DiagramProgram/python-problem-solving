def lists(n):
    arry = []
    for i in range(n):
        x = input()
        if "insert" in x:
            n = x.split()
            a = int(n[1])
            b = int(n[2])
            arry.insert(a, b)
        elif "remove" in x:
            n = x.split()
            a = int(n[1])
            arry.remove(a)
        elif "append" in x:
            n = x.split()
            a = int(n[1])
            arry.append(a)
        elif x == "print":
            print(arry)
        elif x == "sort":
            arry.sort()
        elif x == "pop":
            arry.pop()
        elif x == "reverse":
            arry.reverse()

n = int(input())
lists(n)
