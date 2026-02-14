# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")
for item, data in inventory.items() :
    current_stock = data[0]
    minimum_stock = data[1]
    restock_quantity = data[2]
    sale_status = data[3]
    while current_stock < minimum_stock :
        current_stock += restock_quantity
    inventory[item][0] = current_stock;
    if current_stock > discount_threshold and not sale_status :
        inventory[item][3] = True
    print(f"Processing {item}", data)

print("Processing completed")




        
    