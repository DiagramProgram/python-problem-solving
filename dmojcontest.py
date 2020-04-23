def mavsContest(l1, l2):
    l1x1, l1y1, l1x2, l1y2 = map(int, l1.split())

    if l1y1 == l1y2:
        slope1 = 0
        #y=l1y1 is the equation --> horz line
    elif l1x1 == l1x2:
        slope1 = None
        #slope undefined
        #x = l1x1 --> vert. line
    else:
        slope1 = (l1y2-l1y1) / (l1x2-l1x1)

        b1 = 0
        if l1y1 > slope1*l1x1:
            while l1y1 != slope1*l1x1+b1:
                b1+=1
        elif slope1*l1x1 > l1y1:
            while l1y1 != slope1*l1x1+b1:
                b1-=1
        else:
            b1 = 0
        #print(b1)


    #same thing for second line
    l2x1, l2y1, l2x2, l2y2 = map(int, l2.split())

    if l2y1 == l2y2:
        slope2 = 0
        #y=l2y1 is the equation --> horz line
    elif l2x1 == l2x2:
        slope2 = None
        #slope undefined
        #x = l2x1 --> vert. line
    else:
        slope2 = (l2y2-l2y1) / (l2x2-l2x1)

        b2 = 0
        if l2y1 > slope2*l2x1:
            while l2y1 != slope2*l1x1+b2:
                b2+=1
        elif slope2*l2x1 > l2y1:
            while l2y1 != slope2*l1x1+b2:
                b2-=1
        else:
            b2 = 0
        #print(b2)


    xcoord = 0
    ycoord = 0
    #comparisions
    if slope1 == slope2 and b1 == b2:
        print("coincident")
    elif slope1 == slope2 and b1 != b2:
        print("parallel")
    else:
        xcoord = (b2-b1)/(slope1-slope2)
        ycoord = ((slope2*b1/slope1)-b2) / ((slope2/slope1)-1)
        xc = "%.6f" % xcoord
        yc = "%.6f" % ycoord
        print(str(xc) + " " + str(yc))

l1 = input()
l2 = input()
mavsContest(l1, l2)
