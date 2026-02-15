# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

def apply_discount(prices) :
    prices_copy = prices.copy()
    for index in range(len(prices_copy)) :
        if prices_copy[index] > 2.00 :
            prices_copy[index] *= 0.9
    return prices_copy


# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

print("Updated product prices:", updated_prices)