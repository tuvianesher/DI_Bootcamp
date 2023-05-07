while True:
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        if number % 2 == 0:
            print("The number is even")
        else:
            print("The number is odd")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
