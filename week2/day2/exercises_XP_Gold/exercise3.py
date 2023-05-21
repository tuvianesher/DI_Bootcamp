names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# Ask user for name input
user_name = input("Enter your name: ")

# Check if user name is in the names list
if user_name in names:
    # Get the index of the first occurrence of the user name
    index = names.index(user_name)
    print(f"The index of the first occurrence of {user_name} is {index}.")
else:
    print(f"{user_name} is not in the list.")
while True:
    user_input = input("Press q to quit: ")
    if user_input.lower() == "q":
        break
