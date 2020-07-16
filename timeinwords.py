singles = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
ot = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
teens = ["thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
wholes = ["twenty", "thirty", "fourty", "fifty"]

def timeInWords(h, m):
    if m == 00:
        print(str(singles[h-1]) + " o' clock")
    elif m == 30:
        print("half past " + str(singles[h-1]))
    elif m == 15:
        print("quarter past " + str(singles[h-1]))
    elif m == 45:
        print("quarter to " + str(singles[h])) #h
    elif m == 1:
        print("one minute past " + str(singles[h-1]))
    elif m == 59:
        print("one minute to " + str(singles[h-1]))
    elif m < 30:
        if m <= 12:
            print(str(ot[m-1]) + " minutes past " + str(singles[h-1]))
        elif m <= 19:
            print(str(teens[m-11]) + " minutes past " + str(singles[h-1]))
        elif m < 30:
            print("twenty " + str(singles[m-21]) + " minutes past" + " " + str(singles[h-1]))
    elif m > 30:
        if m < 40:
            a = 60-m
            print("twenty " + str(singles[a-21]) + " minutes to " + str(singles[h]))
        elif m < 50:
            b = 60-m
            print(str(teens[b-13]) + " minutes to " + str(singles[h])) #h
        elif m < 60:
            c = 60-m
            print(str(singles[c-1]) + " minutes to " + str(singles[h])) #h



h = int(input())
m = int(input())
timeInWords(h, m)