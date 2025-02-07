#task 1
class MyClass:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())
        
#task 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2
    
#task 3
class Rectangle(Shape):
    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError()
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b
    
#task 4
class Point:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def show(self):
        print("Координаты точки: (" + str(self.a) + ", " + str(self.b) + ")")

    def move(self, x, y):
        self.a = x
        self.b = y

    def dist(self, p):
        x1 = self.a
        y1 = self.b
        x2 = p.a
        y2 = p.b
        d = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5
        return d

p1 = Point(1, 2)
p2 = Point(4, 6)

p1.show()
p2.show()

p1.move(5, 5)
p1.show()

print("Расстояние:", p1.dist(p2))

#task 5
class Account:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} зачислено! Баланс: {self.balance}")
        else:
            print("Нельзя внести отрицательную сумму")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Недостаточно средств! Баланс: {self.balance}")
        elif amount <= 0:
            print("Нельзя снять отрицательную сумму")
        else:
            self.balance -= amount
            print(f"{amount} снято! Баланс: {self.balance}")

#task 6
from functools import reduce

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

nums = list(range(1, 20))
primes = list(filter(lambda x: is_prime(x), nums))

print(primes)