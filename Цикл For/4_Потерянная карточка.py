n = int(input())
sum_n = 0
for i in range(1, n + 1):
    sum_n += i

sum = 0
for i in range(n - 1):
    card = int(input())
    sum += card
print(sum_n - sum)