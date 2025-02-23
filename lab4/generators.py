def square_generator(n):
    for i in range(n + 1):
        yield i * i

n = int(input("Enter a number n: "))

for square in square_generator(n):
    print(square, end=" ")
    
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter a number n: "))

evens = ", ".join(str(num) for num in even_generator(n))
print(evens)

def div_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number n: "))

for num in div_3_and_4(n):
    print(num, end=" ")
    
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a = int(input("Enter the start number a: "))
b = int(input("Enter the end number b: "))

for value in squares(a, b):
    print(value, end=" ")