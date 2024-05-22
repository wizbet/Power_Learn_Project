def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return price

# Example usage:
original_price = 100
discount_percentage = 25
final_price = calculate_discount(original_price, discount_percentage)
print(f"Final price after {discount_percentage}% discount: ${final_price:.2f}")
