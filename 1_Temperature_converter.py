def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

print("=== Temperature Converter ===")

f = float(input("Enter Fahrenheit: "))
print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")