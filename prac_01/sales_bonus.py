"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
LOW = 0.1
HIGH = 0.15
DIVIDE = 1000
while sales >= 0:
    if sales < DIVIDE:
        bonus = sales * LOW
    else:
        bonus = sales * HIGH
    print(f"Bonus is {bonus}$")
    sales = float(input("Enter sales: $"))

print("Invalid Number")




