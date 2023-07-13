import random
import string

def generate_password(length):
    digits = string.digits
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    special_characters = string.punctuation

    # Ensure each category is included in the password
    password = random.choice(digits) + random.choice(lowercase_letters) + random.choice(uppercase_letters) + random.choice(special_characters)

    # Generate the remaining characters
    remaining_length = length - 4
    password += ''.join(random.choice(digits + lowercase_letters + uppercase_letters + special_characters) for _ in range(remaining_length))

    # Shuffle the password to make it more random
    password = ''.join(random.sample(password, len(password)))

    return password

def validate_password(password):
    has_digit = any(char.isdigit() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_special = any(char in string.punctuation for char in password)
    return has_digit and has_lowercase and has_uppercase and has_special

def test_password(length):
    password = generate_password(length)
    if len(password) != length:
        return False
    if not validate_password(password):
        return False
    return True

# Test the password generation and validation
valid_passwords = 0
for _ in range(100):
    length = random.randint(6, 30)
    if test_password(length):
        valid_passwords += 1

print(f"Out of 100 passwords generated, {valid_passwords} passwords met the requirements.")
