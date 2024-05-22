def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return price

# Get input from the user
original_price = float(input("Enter the original price: $      "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price != original_price:
    print(f"Final price after {discount_percentage}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Original price: ${original_price:.2f}")
