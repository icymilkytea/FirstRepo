class Animal:
    def __init__(self,name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

animals = [Dog("Robin"), Cat("Pipa")]
for i in animals:
    print(i.speak())
#robin = Dog("Robin")
##pipa = Cat("Pipa")

#print(robin.speak())
#print(pipa.speak())


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

# Напишите тут ваш код
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    def drive(self):
        return f"{self.brand} {self.model} is driving."

class Motorcycle(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model
    def ride(self):
        return f"{self.brand} {self.model} is driving."

# Примеры использования классов:
car = Car("Toyota", "Corolla")
print(car.drive())  # Output: Toyota Corolla is driving.

motorcycle = Motorcycle("Yamaha", "R1")
print(motorcycle.ride())  # Output: Yamaha R1 is riding.