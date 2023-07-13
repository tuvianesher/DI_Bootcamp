import re

def return_numbers(string):
    numbers = re.findall(r'\d+', string)
    return int(''.join(numbers))

string = 'k5k3q2g5z6x9bn'
numbers = return_numbers(string)
print(numbers)
