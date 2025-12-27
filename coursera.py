discount = 0.2  # 20% discount
price = 35
final_price = price * (1 - discount)

print(final_price)

if ordertotal >= 50:
  print("Congratulations! You qualify for free shipping.")
else:
  print("Add more items to your cart to reach the free shipping threshold!")
