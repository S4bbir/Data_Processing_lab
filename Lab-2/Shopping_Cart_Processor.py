cart = [
    {"name": "Laptop", "price": 3000, "quantity": 1},
    {"name": "Mouse", "price": 1000, "quantity": 3},
    {"name": "Keyboard", "price": 2500, "quantity": 5},
    {"name": "Headphone", "price": 3000, "quantity": 3}
    ]

total = 0
for product in cart:
    cost = product["price"] * product["quantity"]
    total += cost


def apply_discount(total):
    if total >= 2000:
        return (total - ( total * 0.1))
    else:
        return total

final_price = apply_discount(total)

print("Total Cost:", total)
print("Final Price:", final_price)