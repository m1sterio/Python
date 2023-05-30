lst = input().split(", ")

def all_digits(arr):
    flag = True
    for i in arr:
        if not(i.replace("-", "").isdigit()):
            flag = False
    return flag

def sm(arr):
    result = 0
    if all_digits(arr):
        for i in arr:
            result += int(i)
        print("Сумма:", result)
    else:
        return False


def mult(arr):
    result = 1
    if all_digits(arr):
        for i in arr:
            result *= int(i)
        print("Произведение:", result)
    else:
        return False

sm(lst)
mult(lst)



