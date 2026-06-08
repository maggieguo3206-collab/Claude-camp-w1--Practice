def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_advice(bmi):
    if bmi < 18.5:
        return "Underweight", "You may need to eat more. Consider consulting a nutritionist."
    elif bmi < 25:
        return "Normal", "Great! Keep maintaining a healthy diet and exercise routine."
    elif bmi < 30:
        return "Overweight", "Consider more exercise and a balanced diet."
    else:
        return "Obese", "Please consult a doctor for a personalized health plan."

print("=== BMI Calculator ===")

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m), e.g. 1.75: "))

bmi = calculate_bmi(weight, height)
category, advice = get_advice(bmi)

print(f"\nYour BMI:    {bmi:.1f}")
print(f"Category:    {category}")
print(f"Advice:      {advice}")