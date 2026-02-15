# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for item, data in products.items() :
    price = float(data[0])
    quantity_sold = int(data[1])
    total_sales = price * quantity_sold
    total_sales_list.append(total_sales)
    print(f"Total sales for {item}: ${total_sales}")

total_sum=sum(total_sales_list)
min_sales=min(total_sales_list)
max_sales=max(total_sales_list)

print(f"Total sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")