fruit = input().lower()
day = input().lower()
kg = float(input())

if (fruit == "banana" or fruit == "apple" or fruit == "orange" or fruit == "grapefruit" or fruit == "kiwi" or fruit == "pineapple" or fruit == "grapes") and (day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday" or day == "saturday" or day == "sunday"):
    if day == "saturday" or day == "sunday":
        if fruit == "banana":
            print("%.2f" % (kg * 2.70))
        if fruit == "apple":
            print("%.2f" % (kg * 1.25))
        if fruit == "orange":
            print("%.2f" % (kg * 0.90))
        if fruit == "grapefruit":
            print("%.2f" % (kg * 1.60))
        if fruit == "kiwi":
            print("%.2f" % (kg * 3.00))
        if fruit == "pineapple":
            print("%.2f" % (kg * 5.60))
        if fruit == "grapes":
            print("%.2f" % (kg * 4.20))
    else:
        if fruit == "banana":
            print("%.2f" % (kg * 2.50))
        if fruit == "apple":
            print("%.2f" % (kg * 1.20))
        if fruit == "orange":
            print("%.2f" % (kg * 0.85))
        if fruit == "grapefruit":
            print("%.2f" % (kg * 1.45))
        if fruit == "kiwi":
            print("%.2f" % (kg * 2.70))
        if fruit == "pineapple":
            print("%.2f" % (kg * 5.50))
        if fruit == "grapes":
            print("%.2f" % (kg * 3.85))

else:
    print("error")
