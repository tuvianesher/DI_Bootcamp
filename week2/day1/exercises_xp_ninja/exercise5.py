longest_sentence = ""

while True:
    sentence = input("Enter the longest sentence you can without the character 'A': ")

    if 'A' not in sentence.upper():
        if len(sentence) > len(longest_sentence):
            longest_sentence = sentence
            print("Congratulations! You set a new longest sentence without the character 'A'.")
    else:
        print("Sorry, the sentence contains the character 'A'. Try again.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "no":
        break

print("The longest sentence without the character 'A' is:", longest_sentence)
