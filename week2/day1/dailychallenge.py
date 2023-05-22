import random

# Ask the user for a string
user_input = input("Enter a string (10 characters long): ")

# Check the length of the string
if len(user_input) < 10:
    print("String not long enough")
elif len(user_input) > 10:
    print("String too long")
else:
    # Print the first and last characters
    print("First character:", user_input[0])
    print("Last character:", user_input[-1])

    # Construct the string character by character
    for i in range(1, len(user_input) + 1):
        print(user_input[:i])

    # Bonus: Shuffle the string
    shuffled_string = list(user_input)
    random.shuffle(shuffled_string)
    shuffled_string = ''.join(shuffled_string)
    print("Jumbled string:", shuffled_string)
