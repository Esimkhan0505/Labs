#task 1
def grams_to_ounces(grams):
    return 28.3495231 * grams

print(grams_to_ounces(100))

#task 2
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

print(fahrenheit_to_celsius(100))

#task 3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return None

print(solve(35, 94)) 

#task 4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [n for n in numbers if is_prime(n)]

print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))

#task 5
import itertools

def string_permutations(s):
    return list(map("".join, itertools.permutations(s)))

print(string_permutations("abc"))

#task 6
def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])

print(reverse_sentence("We are ready"))

#task 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))  
print(has_33([1, 3, 1, 3]))  
print(has_33([3, 1, 3])) 

#task 8
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

#task 9
def sphere_volume(radius):
    return (4 / 3) * 3.141592653589793 * (radius ** 3)

print(sphere_volume(3))

#task 10
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

print(unique_elements([1, 2, 2, 3, 4, 4, 5]))

#task 11
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome("madam"))  
print(is_palindrome("hello")) 

#task 12
def histogram(lst):
    for num in lst:
        print("*" * num)

histogram([4, 9, 7])

#task 13
def guess_the_number():
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    attempts = 0
    while True:
        guess = int(input("Take a guess.\n"))
        attempts += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break



