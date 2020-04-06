#from Waterloo's CCC Contest :,(
def arrivaltime(a):
    x = a.split(":")
    hourmin = []
    for each in x:
        p = int(each)
        hourmin.append(p)
    print(hourmin)
    if hourmin[0] not in range(7,11) and hourmin[0] not in range(15,20) and hourmin[0]+2 not in range(8,11) and hourmin[0]+2 not in range(16,20):
        arrival_hrs = hourmin[0]+2
        if hourmin[1] == 0:
            print(str(arrival_hrs) + ":" + str(hourmin[1]) + "0")
        elif hourmin[0]+2 == 7 or hourmin[0]+2 == 15 and hourmin[1] > 0:
            if hourmin[1]*2 < 60:
                print(str(arrival_hrs) + ":" + str(hourmin[1]*2))
            else:
                d = arrival_hrs+1
                e = hourmin[1]*2-60
                print(str(d) + ":" + str(e))
        else:
            print(str(arrival_hrs) + ":" + str(hourmin[1]))
    else:
        arrivaltim = hourmin[0]+4
        if hourmin[0] == 15 and hourmin[1] == 0:
            print(str(arrivaltim) + ":" + str(hourmin[1]) + "0")
        elif hourmin[0] == 15 and hourmin[1]*2 < 60:
            print(str(arrivaltim) + ":" + str(hourmin[1]*2))
        elif hourmin[0] == 15 and hourmin[1]*2 > 60:
            d = arrivaltim+1
            e = hourmin[2]*2-60
            print(str(d) + ":" + str(e))





arrivaltime("07:00")