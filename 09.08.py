class Animal:
    def speak(self):
        return "Ррррррр!"

class Dog(Animal):
    def speak(self):
        parent_speach = super().speak()
        return f"{parent_speach}, Гав"

dog = Dog()
print(dog.speak())


import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method!")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        s = math.pi * self.radius ** 2
        return s


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        s = self.width * self.height
        return s

shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
areas = [shape.area() for shape in shapes]

for area in areas:
    print(area)


class Animal:
    pass

class Cat(Animal):
    pass

class Dog(Animal):
    pass

def check_type(i, j):
    return(isinstance(i,j))
cat = Cat()
dog = Dog()

print(check_type(cat, Animal))
print(check_type(dog, Animal))