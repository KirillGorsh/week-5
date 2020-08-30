# Classes - Chapter 9
# Class - general template, where you have description and behaviour anything you wanted to represent
# class name always starts with capital letter

class Dog():
    """This is the general class about Dog."""
    # Attribute(properties)
    breed = ''
    name = ''


    # Behaviour, methods
    def bark(self):
        print("wouf wouf!!")


class NewDog():
    """This is the general class about Dog."""
    # Attribute(properties)
    breed = ''
    name = ''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("constructing the Dog class.")

    # Behaviour, methods
    def bark(self):
        print(f"{self.name} is barking : wouf wouf!!")


# Object is the instance(representation in specific way) of class
dog1 = Dog()  # mydog is the object of Dog() class
dog1.breed = 'German shepard'
dog1.name = 'Rex'
#dog1.bark()

dog2 = Dog()
dog2.name = "Bobik"
dog2.breed = 'pudo'
# dog2.bark()

print('Name of dog1', dog1.name)
print('Breed of dog1', dog1.breed)
dog1.bark()

print('Name of dog2', dog2.name)
print('Breed of dog2', dog2.breed)
dog2.bark()

dog3 = NewDog('Sharik', 4)
dog3.bark()
dog4 = NewDog('Hatika', 3)
dog4.bark()