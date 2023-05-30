lst = input().replace(" ", "").replace(",", "")
result = []
for i in lst:
    result.append(i)

def reverse_1(ls):
    result = ls[::-1]
    return result

def reverse_2(ls):
    result = list()
    for i in range(len(ls)):
        result.append(ls.pop())
    return result

def lst_out(ls):
    lenght = len(ls)
    for i in range(lenght):
        if i == lenght - 1:
            print(ls[i])
        else:
            print(ls[i], end=", ")

lst_out(reverse_1(result))
lst_out(reverse_2(result))
