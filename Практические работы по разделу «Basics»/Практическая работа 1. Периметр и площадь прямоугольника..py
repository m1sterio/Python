x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

length = abs(x2 - x1)
height = abs(y2 - y1)

area = length * height
perimeter = 2 * (length + height)

print("%.2f" % area)
print("%.2f" % perimeter)