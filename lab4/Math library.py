#1
import math

degrees = float(input("Input degree: "))

radians = degrees * (math.pi / 180)

print("Output radian:", radians)
#2
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = 0.5 * (base1 + base2) * height

print("Expected Output:", area)

#3
import math

n = int(input("Input number of sides: "))
side = float(input("Input the length of a side: "))

area = (n * side ** 2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is:", area)

#4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height

print("Expected Output:", area)
