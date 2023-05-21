alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in alphabet:
    if letter in "aeiou":
        print(letter + " is a vowel")
    else:
        print(letter + " is a consonant")
while True:
    user_input = input("Press q to quit: ")
    if user_input.lower() == "q":
        break
