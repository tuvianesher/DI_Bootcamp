import re

def validate_name(name):
    pattern = r'^[A-Z][a-z]+ [A-Z][a-z]+$'
    return re.match(pattern, name)

full_name = input("Enter your full name: ")
if validate_name(full_name):
    print("Valid name")
else:
    print("Invalid name")
