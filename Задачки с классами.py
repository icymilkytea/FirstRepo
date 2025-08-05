class Cat:
    pass

cat1 = Cat()
cat1.name = "Pepper"
cat1.age = 3

print(f"Имя кошки {cat1.name}. Возраст кошки {cat1.age}")

class Dog:
    def initialize(self, name, age):
        self.name = name
        self.age = age

rex = Dog()
rex.initialize("Rex", 4)
print(f"Кличка собаки {rex.name}, возраст пса {rex.age}")

class spynx:
    name = ''
    age = 0

sansa = spynx()
sansa.name = "Sansa"
sansa.age = 3
print(f"Кличка {sansa.name}, возраст {sansa.age}")

class Reptile:
    def __init__(self, name, age):
        self.name = name
        self.age = age

scorpio = Reptile("SubZero", 133)

print(f"{scorpio.name}, {scorpio.age}")


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        s = self.width * self.height
        return s


treg = Rectangle(5, 4)
print(treg.area())


class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.initial_balance = initial_balance

    def deposit(self, amount):
            self.initial_balance += amount
            print(self.initial_balance)

    def withdraw(self, amount):
            self.initial_balance -= amount
            print(self.initial_balance)


user1 = BankAccount(1, 300)

user1.deposit(20)
user1.withdraw(40)