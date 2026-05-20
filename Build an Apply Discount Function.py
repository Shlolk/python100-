def apply_discount(price, discount):

    # Check if price is a number
    if not isinstance(price, (int, float)):
        return "The price should be a number"

    # Check if discount is a number
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"

    # Check if price is greater than 0
    if price <= 0:
        return "The price should be greater than 0"

    # Check if discount is between 0 and 100
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    # Calculate final price after discount
    final_price = price - (price * discount / 100)

    return final_price


# Test cases
print(apply_discount(100, 20))      # 80
print(apply_discount(200, 50))      # 100
print(apply_discount(50, 0))        # 50
print(apply_discount(100, 100))     # 0
print(apply_discount(74.5, 20.0))   # 59.6

# Error cases
print(apply_discount("hello", 20))
print(apply_discount(100, "ten"))
print(apply_discount(0, 20))
print(apply_discount(100, 120))
