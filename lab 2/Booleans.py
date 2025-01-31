#Example 1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Example 2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
#Example 3 Evaluate a string and a number
print(bool("Hello"))
print(bool(15))

#Example 4 Evaluate two variables
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Example 5 The following will return True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#Example 5 The following will return False  
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({})) 

#Example 6  
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Example 7 Print the answer of a function
def myFunction() :
  return True

print(myFunction())

#Example 8 Print "YES!" if the function returns True, otherwise print "NO!"
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
#Example 9 Check if an object is an integer or not
x = 200
print(isinstance(x, int))