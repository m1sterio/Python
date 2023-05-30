money = 0
while True:
    country = input()
    if country.lower() == "end": break
    need_money = int(input())
    if need_money <= 0:
        print("error")
        break
    while need_money > money:
        plus_money = input()
        if plus_money == "stop":
            exit(0)
        plus_money = int(plus_money)
        if plus_money > 0:
            money += plus_money
    print("Go to " + country + "!")
    money -= need_money
