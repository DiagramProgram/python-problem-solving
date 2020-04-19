nom = []
log = []

def securedoors(n, e, name):
    if e == "entry" and nom.count(name) == 0:
        print(name + " entered")

    elif e == "exit" and nom.count(name) == 0:
        print(name + " exited (ANOMALY)")
    
    elif e == "entry" and nom.count(name) >= 1:
        backnom = list(reversed(nom))
        backlog = list(reversed(log))
        num = backnom.index(name)
        if backlog[num] == "entry":
            print(name + " entered (ANOMALY)")
        else:
            print(name + " entered")
    
    elif e == "exit" and nom.count(name) >= 1:
        backnom = list(reversed(nom))
        backlog = list(reversed(log))
        num = backnom.index(name)
        if backlog[num] == "exit":
            print(name + " exited (ANOMALY)")
        else:
            print(name + " exited")
    
    nom.append(name)
    log.append(e)


n = int(input())

for each in range(n):
    e, name = input().split()
    securedoors(n, e, name)
