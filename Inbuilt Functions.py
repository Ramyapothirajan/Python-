# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 23:12:40 2023

@author: RamyaRajaLakshmi
"""
#Python program to add two numbers
a = int(input("number1:"))
b = int(input("number2:"))
sum_out = a + b
print("The sum of {} and {} is {}".format(a, b, sum_out))

#Python Program for n-th Fibonacci number
num = int(input("Enter a number :"))
def fibonacci(num):
    if num <= 0:
        return "an incorrect input"
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

fib = fibonacci(num)
print(f"The {num}th Fibonacci number is {fib}")



#to check a prime number 

n = int(input("Enter a number:"))
if n > 1:         # Check if number is less than 2, n<2
    for i in range(2, int(n/2)+1):      #range(2, n//2)
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
# If the number is less than 1, its also not a prime number.
else:
    print(n, "is not a prime number")
    
#to check a prime number 
n = int(input("Enter a number:"))
if n > 1:
    for i in range(2,n):
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
# If the number is less than 1, its also not a prime number.
else:
    print(n, "is not a prime number")    
    
    
    
    
    
#inbuilt functions

print(abs(-5))   # Output: 5
print(abs(5))    # Output: 5

print(all([True, True, False]))    # Output: False
print(all([True, True, True]))     # Output: True
print(all([]))                     # Output: True

print(any([False, False, True]))   # Output: True
print(any([False, False, False]))  # Output: False
print(any([]))                     # Output: False

print(ascii('hello'))    # Output: 'hello'
print(ascii('héllo'))    # Output: 'h\xe9llo'


x=5
def test_function():
    y = 10
    print("Local variables:", locals())  
    print("Global variables:", globals())  
test_function()

# create a new module
import types
my_module = types.ModuleType('my_module')

# add a variable to the module
my_module.my_var = 10

# print the global variables of the module
print(globals(my_module))


    












