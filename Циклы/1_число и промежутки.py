while True:
    n = float(input())
    if -300 <= n <= 300 or 1000 <= n <= 1600:
        print("The number is:", n)
        break
    else:
        print("Invalid number!")