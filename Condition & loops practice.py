# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 20:00:34 2023

@author: RamyaRajaLakshmi
"""


a=2;b=3
'p' + 'q' if '12'.isdigit() else 'r' + 's'
#if Statement
a=56
b=23
if b>a:
    print(b-a)
 
name=input("Type your name ")
age=45 
if name.isalpha():
    print("My name is {0}".format(name))
else:
    print("The age of %s is %d"%(name,age))

print("The name is {0} & the age is {1}".format(name,age))    
 
    
a=56
b=23
c=92
if a>b and a>c:
    print(a, "is the largest number")  
elif b>a and b>c:
    print(b, "is the largest number")  
else:
    print(c, "is the largest number")  

num = int(input("Enter the number : "))

if(num > 0 ):
    if(num%5==0):
        print ("The given number is positive and also divisible by 5")
    else:
        print("The given number is positive but not divisible by 5")
elif(num<0):
    if(num%5==0):
        print ("The given number is negative and also divisible by 5")
    else:
        print("The given number is negative but not divisible by 5")
else:
    print("The given number is 0 which cannot be divisible by any number")
    
        
    
age = abs(int(input("Enter your age: ")))

if(age<10):
    print("Children")
elif(age>10 and age<60):
    print("Normal Citizen")
else:
    print("Senior Citizen")

g="Ramya"
g.casefold() #lowercasing but more aggressive because it is intended to remove all case distinctions in a string.
print(g)

gender = str(input("Enter the gender: "))
gender = gender.lower()
age=abs(int(input("Enter your age : "))) 
Fare=abs(int(input("Total fare of a ticket : "))) 
 
if gender == "male" :
    if age <60 : 
        Fare *= 70
        print("The fare of a train ticket is",Fare)
    else:
        Fare *= 1
        print("The fare of a train ticket is",Fare)
elif gender == "female":
    if age < 60 :
        Fare *= 0.7
        print("The fare of a train ticket is",Fare)
    else:
        Fare *= 0.5
        print("The fare of a train ticket is",Fare)
    
    

name = str(input("What is your name? "))
if name != str:
    input("Thats not your name! Please retype your name")
else: 
    print("Hello " + name)

input("Press any button to close")
   
a=5+2
print(a)
id(a)
a=9
id(a)

str="Ramya"
id(str)
str="Ravi"
id(str)

a=42
a.__class__

my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i)

num = 1
for i in range(1,num):
    print(num)

my_list = [1, 2, 3, 4, 5]
for i in enumerate(my_list):
    print(i)
    
list1=[1,5.5,(10+20j),'data science']
for i in enumerate(list1):
    print(i)
print(list1.count(1))   
print(len(list1))
print(list1.index(10+20j))
list1.reverse()
print(list1)

list1=[1,5.5,(10+20j),'data science']
list1.append(4)
print(list1)
list1.remove(5.5)
print(list1)
print(list1.pop(2))
print(list1)
list1.insert(1,"Apple")
print(list1)



#print(min(list1))
#print(max(list1))
#print(sorted(list1))
#print(sum(list1))

l = list(reversed(list1))
print (l)

var1=tuple(range(0,10))
print(var1)

var2=set(range(3,20,3))
print(var2)

i = int(input("Enter number : "))
output = list(range(1,i+1))
print(output)

list1 = [3,4,5,6,7,8]
list2 = []
for i in list1:
    if i%2==0:
        list2.append(i+10)
    else:
        list2.append(i*5)
     
print(list2)

#zip() function is used to combine the two lists into pairs of elements
l1=[1,2]
l2=['on','ty']
for i,j in zip(l1,l2):
    print(i,':',j)

my_list = ['a', 1, 'b', 2, 'c', 3]
my_dict = {my_list[i]: my_list[i+1] for i in range(0, len(my_list), 2)}

print(my_dict)  # prints {'a': 1, 'b': 2, 'c': 3}



l1 = [1,2,3]
l2=['one','two','three']
# Convert the zip object to a list of tuples
l3 = list(zip(l1, l2))
print(l3)  # prints [(1, 'one'), (2, 'two'), (3, 'three')]
t=tuple(zip(l2,l1))
print(t)
# Convert the zip object to a dictionary
d1 = dict(zip(l1, l2))
print(d1)  # prints {1: 'one', 2: 'two', 3: 'three'}


list_1=list(range(0,10))
list_2=['zero','one','two','three','four','five','six','seven','eight','nine']
dict_1=dict(zip(list_2,list_1))
print(dict_1)

#or 

list_1=list(range(0,10))
list_2=['zero','one','two','three','four','five','six','seven','eight','nine']
dict={}
for i,j in zip(list_2,list_1):
    dict[i]=j
print(dict)

# Define a list of keys and a list of values
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

# Create an empty dictionary
my_dict = {}

# Use a while loop to add key-value pairs to the dictionary
i = 0
while i < len(keys):
    my_dict[keys[i]] = values[i]
    i += 1

print(my_dict)  # prints {'a': 1, 'b': 2, 'c': 3, 'd': 4}


#function
def func(a, b = 5, c = 10):
   print('a is', a, 'and b is', b, 'and c is', c)
func(3, 7)
func(25, c = 24)
func(c = 50, a = 100)

def greet(name,message = "How are you"):
    print("Hi " +name +',' +message)
    
#greet('Ramya', "Hope you are doing good")
greet('Ramya')