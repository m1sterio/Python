sum_simple = 0
sum_non_simple = 0
while True:
    num = input()
    if num.lower() == "stop":
        break
    num = int(num)
    if num == 0:
        print("Number is zero.")
        continue
    if num < 0:
        print("Number is negative.")
        continue
    if num == 1:
        continue
    flag = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            flag = False
            sum_non_simple += num
            break
    if flag:
        sum_simple += num
print("Sum of all prime numbers is:", sum_simple)
print("Sum of all non prime numbers is:", sum_non_simple)