import random

def random_game(user_number):
    random_number = random.randint(1, 100)

    if user_number == random_number:
        print("Congratulations! You guessed the correct number!")
    else:
        print("Sorry, try again next time.")

# You can test the function by calling it with a user-provided number
# For example:
# user_input = int(input("Enter a number between 1 and 100: "))
# random_game(user_input)
