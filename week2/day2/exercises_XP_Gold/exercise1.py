list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)
while True:
    user_input = input("Press q to quit: ")
    if user_input.lower() == "q":
        break
