#!/usr/bin/env python
# coding: utf-8

# In[1]:


def my_function():
    print("hello")
    
my_function()


# In[3]:


def my_function(fname):
    print(fname + " Smith")
    
my_function("Will")
my_function("Sam")


# In[5]:


def my_function(fname, lname):
    print(fname + " " + lname)
    
my_function("Will", "Smith")


# In[8]:


def square(number):
    return number ** 2
squared = square(5.5)
print(squared)
my_number = 6
print(square(my_number))


# In[12]:


# calculate cube of number
import math

def cube(number):
    return pow(number,3)

number = int(input("Enter a number: "))
cubed = cube(number)
print(cubed)


# In[14]:


def my_function(x):
    return 5*x

print(my_function(5))
print(my_function(15))
print(my_function(17))


# In[40]:


# compute the factorial of given number

def factorial(number):
    factorial = 1
    for i in range(2, number+1):
        factorial *= number
        number -=1
        
    return factorial

number = int(input("Enter a number: "))
print(factorial(number))


# In[32]:


# define a function returns the absolute number

def absolute(number):
    if number < 0:
        return -number
    else:
        return number
    
print(absolute(-5))


# In[33]:


def my_function():
    x = 10
    print("inside function" , x)

x = 20
my_function()
print("outside function", x)


# In[36]:


# calculate difference between squared sum of n natural numbers and sum squared first n natural numbers
'''
1+2+3+4+5= 15 (15*15)=225 sum_square
1*1+2*2+3*3+4*4+5*5 = 55  square_sum

225-55
'''

def squared_sum(number):
    sum = 0
    for i in range(number + 1):
        sum += i**2
        
    return sum

def sum_squared(number):
    sum = 0
    for i in range(number + 1):
        sum += i
        
    return sum**2

number = int(input("Enter a number: "))
difference = sum_squared(number) - squared_sum(number)
print(difference)


# In[42]:


# calculate difference between squared sum of n natural numbers and sum squared of first n natural numbers
'''
1+2+3+4+5= 15 (15*15)=225
1*1+2*2+3*3+4*4+5*5 = 55

225-55
'''

def diff_sum(number):
    sum_square = 0
    square_sum = 0
    
    for i in range(number + 1):
        sum_square += i
        square_sum += i**2
        
    sum_square = sum_square **2
    
    return sum_square - square_sum

number = int(input("Enter a number: "))
print(diff_sum(number))


# In[49]:


# convert miles and kilometers
# miles = km / 1.609 
# km = miles * 1.609

def km_to_miles(number):
    return ("distance in miles:", number / 1.609)
    
    
def miles_to_km(number):
    return ("distance in km:" , number * 1.609)

choice = int(input("Enter 1 for km to miles, 2 for miles to km: "))
distance = float(input("Enter the distance: "))

if choice == 1:
    print(km_to_miles(distance))
elif choice == 2:
    print(miles_to_km(distance))
else:
    print("Invalid choice entered")


# In[ ]:




