n = int(input())
count = 1
for i in range(1, n + 1):
    for j in range(1, count):
        print("*", end='\t')
    for q in range(count, n + 1):
        print(q, end='\t')
    count += 1
    print()