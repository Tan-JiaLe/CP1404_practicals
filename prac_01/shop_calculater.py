number = int(input("Number of items: "))
total = 0
for i in range(number):
    price = float(input("Price of item: "))
    total += price
if total > 100:
    total = total * 0.9
    print(f"Total price for {number} items is {total}")
else:
    print(f"Total price for {number} items is {total}")