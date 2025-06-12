import random
import string

def generate_password(length):
    if length < 4:
        return "⚠️ Password should be at least 4 characters long."

    # Combine all character sets
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("🔐 Password Generator 🔐")

    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("⚠️ Please enter a valid number.")
        return

    password = generate_password(length)
    print(f"\n🧾 Generated Password: {password}")

if __name__ == "__main__":
    main()
