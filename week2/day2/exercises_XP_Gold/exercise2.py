for i in range(1500, 2501):
    if i % 5 == 0 and i % 7 == 0:
        print(i)
while True:
    user_input = input("Press q to quit: ")
    if user_input.lower() == "q":
        break
