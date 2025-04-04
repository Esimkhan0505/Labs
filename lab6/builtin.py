from math import prod

def multiply_list(numbers):
    return prod(numbers)


numbers = [2, 3, 4, 5]
result = multiply_list(numbers)
print(f"Произведение чисел {numbers}: {result}")

def count_case(text):
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    return upper, lower


string = "Hello World"
upper, lower = count_case(string)
print(f"Строка: {string}")
print(f"Заглавных букв: {upper}")
print(f"Строчных букв: {lower}")

def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]


string = "Racecar"
print(f"Строка: {string}")
print(f"Палиндром: {is_palindrome(string)}")

import math
import time

def delayed_sqrt(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    return math.sqrt(number)



number = 25100
delay = 2123
result = delayed_sqrt(number, delay)
print(f"result:{result}")



def all_true(tuple_data):
    return all(tuple_data)


tuple1 = (True, 1, "hello")
tuple2 = (True, 0, "hello")
print(f" {tuple1}: {all_true(tuple1)}")
print(f" {tuple2}: {all_true(tuple2)}")