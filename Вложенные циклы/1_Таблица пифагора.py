for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, ' ', end='')
        if (i*j < 10):
            print(' ', end='')
    print()