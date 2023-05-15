class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Fluffy", 5)
cat2 = Cat("Socks", 8)
cat3 = Cat("Whiskers", 3)

def find_oldest_cat(*cats):
    oldest_cat = None
    for cat in cats:
        if oldest_cat is None or cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print("The oldest cat is {}, and is {} years old.".format(oldest_cat.name, oldest_cat.age))
