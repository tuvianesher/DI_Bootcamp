# Ask user for 7 words
words = []
for i in range(7):
    word = input("Enter word #" + str(i+1) + ": ")
    words.append(word)

# Ask user for a single character and clean the input
letter = input("Enter a single letter: ").strip().lower()
if len(letter) != 1:
    print("Please enter only a single letter.")
    exit()

# Loop through the words list
for word in words:
    if letter in word.lower():
        print("Index of first appearance of letter in", word, "is", word.lower().index(letter))
    else:
        print("The letter", letter, "does not appear in the word", word)
while True:
    user_input = input("Press q to quit: ")
    if user_input.lower() == "q":
        break
