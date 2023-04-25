class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + "is now siting")

    def roll_over(self):
        print(self.name.title() + "is rolled over")


my_dog = Dog("weiwei",18)
print(my_dog.name)
print(my_dog.age)
my_dog.sit()
my_dog.roll_over()