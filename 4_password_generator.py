import random
import string

def generate_password(length):
    if length < 8 or length > 24:
        return None
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

print("=== Password Generator ===")

length = int(input("Enter password length (8-24): "))
password = generate_password(length)

if password:
    print(f"\nGenerated Password: {password}")
else:
    print("Invalid length! Please enter a number between 8 and 24.")