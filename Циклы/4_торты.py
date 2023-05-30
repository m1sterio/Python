weight = int(input())
lenght = int(input())

pieces = weight * lenght
count = 0

if 1 <= lenght <= 1000 and 1 <= weight <= 1000:
    while True:
        n = input()
        if n.lower() == "stop":
            if pieces >= count:
                print(pieces - count, "pieces are left.")
                break
        n = int(n)
        count += n
        if pieces <= count:
            print("No more cake left! You need", abs(pieces - count), "pieces more.")
            break