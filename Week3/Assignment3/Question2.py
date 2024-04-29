def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: Ksh "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price after applying the discount
if final_price != original_price:
    print(f"The final price after applying a {discount_percentage}% discount is: Ksh {final_price:.2f}")
else:
    print("No discount applied. The original price remains: Ksh" + str(original_price))
