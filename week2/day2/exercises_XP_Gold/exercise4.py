# Ask the user for 3 numbers
num1 = float(input("Input the 1st number: "))
num2 = float(input("Input the 2nd number: "))
num3 = float(input("Input the 3rd number: "))

# Determine the greatest number
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

# Print the result
print("The greatest number is:", greatest)
while True:
    user_input = input("Press q to quit: ")
    if user_input.lower() == "q":
        break
