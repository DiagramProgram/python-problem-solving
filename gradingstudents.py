n = int(input())

def gradingStudents(n):
    lst = []
    for i in range(n):
        lst.append(int(input()))
    #print(lst)

    for each in lst:
        if (each+1)%5 == 0 and each >= 38:
            print(each+1)
        elif (each+2)%5 == 0 and each >= 38:
            print(each+2)
        else:
            print(each)

gradingStudents(n)