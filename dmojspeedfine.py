l = int(input())
s = int(input())

def checkSpeed(limit, speed):
    if speed <= limit:
        print("Congratulations, you are within the speed limit!")
    elif speed - limit <= 20:
        print("You are speeding and your fine is $100.")
    elif speed - limit <= 30:
        print("You are speeding and your fine is $270.")
    else:
        print("You are speeding and your fine is $500.")

checkSpeed(l, s)