def apply_discount(price, discount=0.05) :
    return price * (1 - discount)

def apply_tax(price, tax = 0.07) :
    return price * (1 + tax)

def calculate_total(price, discount=0.05, tax=0.07) :
    return apply_tax(apply_discount(price, discount), tax)

total_price_default = calculate_total(120)
total_price_custom = calculate_total(100, discount=0.10, tax=0.08)

print(f"Total cost with default discount and tax: ${total_price_default}")
print(f"Total cost with custom discount and tax: ${total_price_custom}")


