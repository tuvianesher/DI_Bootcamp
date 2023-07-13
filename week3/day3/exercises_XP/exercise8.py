# be sure to install faker with pip install faker
from faker import Faker
import random

fake = Faker()
users = []

def add_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': random.choice(['en', 'fr', 'es', 'de'])
    }
    users.append(user)

add_user()
add_user()
add_user()

print(users)
