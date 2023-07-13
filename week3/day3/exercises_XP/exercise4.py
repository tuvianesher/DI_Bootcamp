import string
import random

def generate_random_string():
    letters = string.ascii_letters
    random_string = ''.join(random.choices(letters, k=5))
    return random_string

# You can test the function by calling it
random_str = generate_random_string()
print(random_str)
