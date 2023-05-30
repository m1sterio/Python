degrees = int(input())
day = input().lower()
if 10 <= degrees <= 42:
    if 10 <= degrees <= 18:
        if day == "morning":
            print("It's", degrees, "degrees get your Sweatshirt and Sneakers.")
    elif degrees >= 25:
        print("It's", degrees, "degrees get your Swim Suit and Barefoot.")
    elif (degrees >= 25 and day == "morning") or (18 <= degrees <= 24 and day == "afternoon"):
        print("It's", degrees, "degrees get your T-Shirt and Sandals.")
    else:
        print("It's", degrees, "degrees get your Shirt and Moccasins.")
else:
    print("error")
