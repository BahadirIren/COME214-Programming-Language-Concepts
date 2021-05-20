#!/usr/bin/env python
# coding: utf-8

# In[2]:


b = False

if b :
    print("hello")
else :
    print("its nice to see you")


# In[5]:


print(not a)
print(not b)


# In[7]:


print(a and b)
print(a or b)


# In[9]:


num1 = int(input("Enter a number: "))

if num1 > 0 :
    print(num1 ,"is positive")
else :
    print(num1 ,"is negative")


# In[27]:


# Accepts three sides of a triangle and check whether it is an equilateral, isosceles or scalane triangle
num1 = int(input("Enter first side of the triangle: "))
num2 = int(input("Enter second side of the triangle: "))
num3 = int(input("Enter third side of the triangle: "))

if num1 == num2 and num1 == num3 :
    print("equilateral")
elif num1 != num2 and num2 != num3 and num1 != num3 :
    print("scalane")
else :
    print("isosceles")


# In[41]:


# write a program to accept two numbers and mathematical operators and perform operation accordingly
num1 = int(input("Enter a number: "))
operation = input("Enter operation: (* , / , + , - , ** , //, %): ")
num2 = int(input("Enter a number: "))

if operation == '+' :
    print(num1 + num2)
elif operation == '*' :
    print(num1 * num2)
elif operation == '-' :
    print(num1 - num2)
elif operation == '/' :
    print(num1 / num2)
elif operation == '**' :
    print(num1 ** num2)
elif operation == '//' :
    print(num1 // num2)
elif operation == '%' :
    print(num1 % num2)
else :
    print("invalid operator entered")


# In[ ]:




