#!/usr/bin/env python
# coding: utf-8

# In[5]:


my_name = "Bahadir Iren"
# print("Hello and welcome "+ my_name)
print("Hello and welcome", my_name)


# In[6]:


print("Welcome to Python")
print('Welcome to Python')
print("Welcome","to","Python")
# al is same


# In[7]:


print("Welcome\nto\nPython")


# In[10]:


# comment line
'''
name surname
'''


# In[12]:


print(2+3)  # addition
print(4-2)  # subtraction
print(2*4)  # multiplication
print(65/5) # division
print(137%11) # remainder
print(2**3) # pow


# In[13]:


45+85


# In[14]:


x=45
type(x)


# In[15]:


2+0.5


# In[16]:


x = 2.5
print("x is =",x)


# In[18]:


a = 6
b = 7
result = a + b
print("two times of the result is =", 2 * result)


# In[19]:


print(7/4)
print(7//4) # takes int part


# In[20]:


1660%5


# In[21]:


1.5e2 # e means 10 to the power


# In[24]:


# +,-,*,/ will be evaluated from left to right
# ** will be evaluated from right to left
a = 2
b = 4
c = 5
d = 6
y = a*b**2 + b*d +c
print(y)
y = a*(b**2) + (b*d) + c
print(y)


# In[25]:


print(4**3**2)
print(4**(3**2))
print((4**3)**2)


# In[26]:


# given that y=ax^3+7, express this with different ways

y1 = a*(x**3) + 7
y2 = a*x**3 + 7
y3 = a*pow(x,3) +7

print(y1)
print(y2)
print(y3)


# In[29]:


number1 = 10
number1 += 30
print(number1)
number2 = 10
number2 = number2 + 30
print(number2)


# In[30]:


age = 20
AGE = 30
print(age)
print(AGE) # python sensitive about uppercase


# In[33]:


value1 = int(input("Enter an integer number = "))
value2 = int(input("Eneter another integer number = "))
print("value1 + value2 =", value1 + value2)


# In[39]:


x = 5     # integer
y = 22.5  # float
x = float(x)  # int to float
print(x,type(x))


y = int(y) # float to int
print(y,type(y))


# In[41]:


ceaser = "graham "
praline = "John "
print(ceaser, type(ceaser))
print(praline)


# In[46]:


print(7 > 4)
print(7 < 4)
print(7 <= 4)
print(7 >= 4)
print(7 == 4)
print(7 != 4)


# In[48]:


value1 = int(input("Enter an integer number = "))
value2 = int(input("Eneter an integer number = "))
print(value1 * value2)
print(value1 / value2)
print(value1 // value2)
print(value1 + value2)
print(value1 - value2)
print(value1 < value2)
print(value1 > value2)
print(value1 <= value2)
print(value1 >= value2)
print(value1 == value2)
print(value1 != value2)
print(value1 ** value2)


# In[69]:


from math import pi
area = pi*(pow(float(input("Enter radius r = ")),2))
print(format(area,".3f" )) # with 3 decimal point


# In[ ]:




