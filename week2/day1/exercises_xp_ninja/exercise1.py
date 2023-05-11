import math

# define the values of C and H
C = 50
H = 30

# ask the user for a comma-separated string of numbers
input_string = input("Enter a comma-separated string of numbers: ")

# split the input string into a list of numbers
numbers = input_string.split(",")

# create an empty list to store the results
results = []

# iterate over the numbers list, calculate Q for each number, and append the result to the results list
for num in numbers:
    D = int(num)
    Q = int(math.sqrt((2 * C * D) / H))
    results.append(str(Q))

# print the results as a comma-separated string
print(",".join(results))
