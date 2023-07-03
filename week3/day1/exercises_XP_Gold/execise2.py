import random

class MyList:
    def __init__(self, letters):
        self.letters = letters

    def reverse_list(self):
        return self.letters[::-1]

    def sort_list(self):
        return sorted(self.letters)

    def generate_random_list(self):
        return [random.randint(1, 100) for _ in range(len(self.letters))]

# Create an instance of the MyList class with a list of letters
my_list = MyList(['a', 'b', 'c', 'd', 'e'])

# Reverse the list and print the result
reversed_list = my_list.reverse_list()
print(f"Reversed List: {reversed_list}")

# Sort the list and print the result
sorted_list = my_list.sort_list()
print(f"Sorted List: {sorted_list}")

# Generate a random list and print the result
random_list = my_list.generate_random_list()
print(f"Random List: {random_list}")
