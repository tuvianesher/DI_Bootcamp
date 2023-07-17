import random

def get_random_sentence(length):
    words = get_words_from_file()
    random_words = random.choices(words, k=length)
    sentence = ' '.join(random_words).lower()
    return sentence
def get_words_from_file():
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    return words
def main():
    print("Welcome to the Random Sentence Generator!")
    print("Please enter the length of the sentence (between 2 and 20):")
    length = input()

    # Validate user input
    try:
        length = int(length)
        if length < 2 or length > 20:
            raise ValueError
    except ValueError:
        print("Invalid input! Please enter a valid integer between 2 and 20.")
        return

    # Generate and print the random sentence
    sentence = get_random_sentence(length)
    print("Random Sentence:", sentence)

# Run the main function
if __name__ == '__main__':
    main()
