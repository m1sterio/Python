cinema = input().lower()
r = int(input())
c = int(input())
count = r * c

if cinema == "premiere":
    print("%.2f" % (count * 12), "$")
if cinema == "normal":
    print("%.2f" % (count * 7.5), "$")
if cinema == "discount":
    print("%.2f" % (count * 5), "$")
