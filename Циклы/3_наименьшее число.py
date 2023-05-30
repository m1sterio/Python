mn = 10000000000
n = int(input())
i = 0
if n > 0:
    while i < n:
        num = int(input())
        if num < mn:
            mn = num
        i += 1
    print(mn)
else:
    print("error")