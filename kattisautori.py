def autori(inpt):
    e = inpt.split("-")
    #print(e)
    for each in e:
        print(each[0], end="")


inpt = input()
autori(inpt)