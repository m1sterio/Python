area = float(input())

final_price = area * 7.61
discount = final_price * 0.18
final_price -= discount

print("The final price is:", '%.2f' % final_price, "$.")
print("The discount is:", '%.2f' % discount, "$.")