import random

total_wins = 0
total_losses = 0
keep_playing = True

while keep_playing:
    user_guess = input("Guess a number between 1 and 9 (inclusive) or type 'q' to quit: ")
    
    if user_guess == 'q':
        keep_playing = False
        print("Thanks for playing!")
        break
    
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")
        continue
    
    random_number = random.randint(1, 9)
    
    if user_guess == random_number:
        print("Winner!")
        total_wins += 1
    else:
        print(f"Better luck next time. The correct number was {random_number}.")
        total_losses += 1

print(f"Total games won: {total_wins}")
print(f"Total games lost: {total_losses}")
