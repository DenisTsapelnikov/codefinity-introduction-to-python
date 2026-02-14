prices = [29.99, 45.50, 12.75, 38.20]

for price in range(len(prices)) :
    if price == 0 :
        prices[price] *= 0.9
    elif price == 1 :
        prices[price] *= 0.8
    elif price == 2 :
        prices[price] *= 0.85
    elif price == 3 :
        prices[price] *= 0.95
    print(f"Updated price for item {price}: ${prices[price]:.2f}")