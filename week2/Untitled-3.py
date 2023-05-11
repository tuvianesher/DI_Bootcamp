number = int(input("Enter a number: "))
length = int(input("Enter the length of the list: "))

multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)

print(multiples)
