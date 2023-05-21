# Create a list of numbers from 1 to 1 million
numbers = list(range(1, 1000001))

# Check that the list starts at 1 and ends at 1 million
print("Minimum number in the list:", min(numbers))
print("Maximum number in the list:", max(numbers))

# Use the sum() function to see how quickly Python can add a million numbers
print("Sum of the numbers in the list:", sum(numbers))
while True:
    user_input = input("Press q to quit: ")
    if user_input.lower() == "q":
        break
