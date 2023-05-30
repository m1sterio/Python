st1 = input().split()
st2 = input().split()


def same_items(s1, s2):
    flag =True
    for i in s2:
        for j in s1:
            if i.lower() == j.lower():
                print(i, end=" ")
                flag = False
    if flag:
        print("No matches!")


same_items(st1, st2)
