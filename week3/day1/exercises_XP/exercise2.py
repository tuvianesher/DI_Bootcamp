class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        
    def bark(self):
        print("{} goes woof!".format(self.name))
        
    def jump(self):
        print("{} jumps {} cm high!".format(self.name, self.height*2))

# create davids_dog object
davids_dog = Dog("Rex", 50)
print("David's dog is {} and is {} cm tall.".format(davids_dog.name, davids_dog.height))
davids_dog.bark()
davids_dog.jump()

# create sarahs_dog object
sarahs_dog = Dog("Teacup", 20)
print("Sarah's dog is {} and is {} cm tall.".format(sarahs_dog.name, sarahs_dog.height))
sarahs_dog.bark()
sarahs_dog.jump()

# compare the sizes of the two dogs
if davids_dog.height > sarahs_dog.height:
    print("{} is bigger than {}.".format(davids_dog.name, sarahs_dog.name))
elif sarahs_dog.height > davids_dog.height:
    print("{} is bigger than {}.".format(sarahs_dog.name, davids_dog.name))
else:
    print("{} and {} are the same height.".format(davids_dog.name, sarahs_dog.name))
