money = int(input())
season = input().lower()
fishermans = int(input())
price = 0
if 1 <= money <= 8000 and 4 <= fishermans <= 18:
    if season == "spring":
        if fishermans <= 6:
            price = 3000 * 0.9
        if 7 <= fishermans <= 11:
            price = 3000 * 0.85
        if fishermans >= 12:
            price = 3000 * 0.75
            
    if season == "summer" or season == "autumn":
        if fishermans <= 6:
            price = 4200 * 0.9
        if 7 <= fishermans <= 11:
            price = 4200 * 0.85
        if fishermans >= 12:
            price = 4200 * 0.75

    if season == "winter":
        if fishermans <= 6:
            price = 2600 * 0.9
        if 7 <= fishermans <= 11:
            price = 2600 * 0.85
        if fishermans >= 12:
            price = 2600 * 0.75

    if fishermans % 2 == 0 and not(season == "autumn"):
        price *= 0.95

    if money >= price:
        print("Yes! You have", "%.2f" % (money - price), "rubles left.")

    if money <= price:
        print("Not enought money! You need","%.2f" % (price - money),"rubles.")

else:
    print("error")
