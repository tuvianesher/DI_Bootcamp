# Ask user for inputs 5 times and create a list of tuples
data = [(input("Name: "), int(input("Age: ")), int(input("Score: "))) for _ in range(5)]

# Sort the list by Name > Age > Score
sorted_data = sorted(data, key=lambda x: (x[0], x[1], x[2]))

print(sorted_data)
