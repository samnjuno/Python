def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

# values
original_price = 100
discount_percent = 25

# Call the function to calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Output the final price
print(f"The final price after applying the discount is: ${final_price:.2f}")
