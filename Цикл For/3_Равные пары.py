n = int(input())

sm = 0
mx = -10000000000
flag = True

for i in range(n):
    n1 = int(input())
    n2 = int(input())

    if i == 0:
        sm = n1 + n2
    else:
        curr_sm = n1 + n2
        if abs(sm - curr_sm) > mx and abs(sm - curr_sm) != 0:
            mx = abs(sm - curr_sm)
            flag = False
    sm = n1 + n2

if flag:
    print("Yes, value =", sm)
else:
    print("No, maxdiff =", mx)

