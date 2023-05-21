# Ask the user for input of comma-separated numbers
numbers_input = input("Enter comma-separated numbers: ")

# Split the input string into a list of strings
numbers_list = numbers_input.split(",")

# Convert the list of strings into a tuple
numbers_tuple = tuple(numbers_list)

# Print the list and tuple
print(numbers_list)
print(numbers_tuple)
