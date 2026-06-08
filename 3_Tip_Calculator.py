def calculate_tip(meal_cost, tip_percent):
    tip_amount = meal_cost * (tip_percent / 100)
    total = meal_cost + tip_amount
    return tip_amount, total

print("=== Tip Calculator ===")

meal_cost = float(input("Enter meal cost: $"))
tip_percent = float(input("Enter tip percentage: %"))

tip_amount, total = calculate_tip(meal_cost, tip_percent)

print(f"\nMeal Cost:   ${meal_cost:.2f}")
print(f"Tip ({tip_percent:.0f}%):    ${tip_amount:.2f}")
print(f"Total Cost:  ${total:.2f}")