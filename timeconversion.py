def timeConversion(s):
    hour, min, secampm = s.split(":")
    secampm = secampm[:2]
    if "AM" in s:
        if hour == "12":
            hour = "00"
            print(hour + ":" + min + ":" + secampm)
        else:
            s = s[:8]
            print(s)
    else:
        if hour == "12":
            print(hour + ":" + min + ":" + secampm)
        else:        
            hour = str(int(hour)+12)
            print(hour + ":" + min + ":" + secampm)

s = input()
timeConversion(s)