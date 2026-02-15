# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

for item, data in inventory.items() :
    if (data[0] < 30) :
        print(f"{item} need restocking.")
    elif (data[0] > 100) :
        print(f"{item} should be sold at the discounted price of {data[2]}.")
    else :
        print(f"{item} should be sold at the regular price of {data[1]}.")