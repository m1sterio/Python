n = int(input())
addresses = []

if n <= 0:
    print("error")
    exit(0)


for i in range(n):
    address = input()
    addresses.append(address)


def four_elem(arr):
    flag = True
    for i in arr:
        if len(i.split(".")) != 4:
            return False
    return flag


def ip_correct(arr):
    flag = True
    for i in arr:
        i.split(".")
        if i.count("255") > 3 or i[0] == "0":
            flag = False
            return flag
    return flag


def ip_correct_interval(arr):
    flag = True
    for i in arr:
        i = i.split(".")
        for j in i:
            if int(j) < 0 or int(j) > 255:
                flag = False
                return flag
    return flag


def dec(ip):
    ip_address = ip.split(".")
    result = 0
    pow = 3
    for j in ip_address:
        result += (256 ** pow * int(j))
        pow -= 1
    return result


def local_ip(arr):
    flag = False
    for i in arr:
        ip_address = i.split(".")
        if (ip_address[0] == "10" and ip_address[1] == "0") or (
                ip_address[0] == "172" and ip_address[1] == "16") or (
                ip_address[0] == "192" and ip_address[1] == "168"):
            flag = True
    return flag


def sort_ip(arr):
    for j in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if dec(arr[i]) > dec(arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def arr_out(arr):
    for i in arr:
        print(i)

        
if not (four_elem(addresses)):
    print("error")
elif not (ip_correct(addresses)):
    print("error")
elif not(ip_correct_interval(addresses)):
    print("error")
elif local_ip(addresses):
    print("The list contains the local IP!")
elif not (local_ip(addresses)) and four_elem(addresses) and ip_correct(addresses) and ip_correct(addresses):
    arr_out(sort_ip(addresses))
