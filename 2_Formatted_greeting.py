def get_greeting(gender):
    gender = gender.strip().lower()
    if gender in ["male", "m"]:
        return "Mr."
    elif gender in ["female", "f"]:
        return "Ms."
    else:
        return ""

name = input("Enter your name: ").strip()
gender = input("Enter your gender (male/female): ").strip()

title = get_greeting(gender)

if title:
    print(f"\nHello, {title} {name}! Welcome, hope you have a wonderful day!")
else:
    print(f"\nHello, {name}! Welcome, hope you have a wonderful day!")