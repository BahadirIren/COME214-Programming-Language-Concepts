#!/usr/bin/env python
# coding: utf-8

# In[2]:


# nested if statements

x = 15
if x > 10 :
    print("above ten")
    if x > 20 :
        print("and also above 20")
    else :
        print("but not above 20")


# In[8]:


# write a program to find median of three numbers (middle number)

a = float(input("Enter first number"))
b = float(input("Enter second number"))
c = float(input("Enter third number"))

if a > b :
    if a < c :
        median = a
    elif b > c :
        median = b
    else :
        median = c
else :
    if a > c :
        median = a
    elif b < c :
        median = b
    else :
        median = c
print("The median is", median)
        


# In[3]:


# write a program that reads two integers representing a month and prints the season for that month and day
'''
input month and day
seasons
winter : 21 December-20 March 
spring : 21 March- 20 June    
summer : 21 June - 22 September  
autumn : 23 September - 20 December
'''

day = int(input("Enter day: "))
month = int(input("Enter month: "))
valid = True

if month == 12 and day >= 21 or month == 3 and day <= 20 or month >= 1 and month < 3:
    season = "Winter"
elif month == 3 and day >= 21 or month == 6 and day <= 20 or month > 3 and month < 6:
    season = "Spring"
elif month == 6 and day >= 21 or month == 9 and day <= 22 or month > 6 and month < 9:
    season = "Summer"
elif month == 9 and day >= 23 or month == 12 and day <= 20 or month > 9 and month < 12: 
    season = "Autumn"
else:
    print("Wrong number entered")
    valid = False
    
if valid == True:   
    print("Day:", day, "\nMonth:", month, "\nSeason:", season)


# In[9]:


# for loop

for x in "banana" :
    print(x)


# In[12]:


numbers = [1,2,3,4,5]
for num in numbers:
    print(num)


# In[13]:


numbers = [1,2,3,4,5]

for num in numbers:
    print("Hello")


# In[14]:


fruits = ["apple", "banana", "cherry"]

for x in fruits :
    print(x)


# In[16]:


# check which number is divisible by 3

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]

for num in numbers :
    if num %3 == 0:
        print(num)


# In[18]:


# find square of the odd number
import math

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]

for num in numbers :
    if num % 2 != 0:
        print(math.pow(num,2))


# In[19]:


# sum of the numbers in the list
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]

sum = 0 
for num in numbers:
    sum += num
print(sum)


# In[20]:


# range function, sum of the numbers in the range
x = range(1,13)
sum = 0 
for num in x :
    sum += num
print(sum)


# In[22]:


# range function
x = range(1,20,2) # increment by 2 (odd numbers)
for num in x:
    print(num)


# In[23]:


# range function
x = range(20,2,-2) # decremant by 2
for num in x: 
    print(num)


# In[25]:


x = range(10,-6,-2)
for num in x: 
    print(num)


# In[26]:


x = range(-6,10,2)
for num in x: 
    print(num)


# In[27]:


# reversed function

for i in reversed(range(5)):
    print(i)


# In[28]:


# normal order
for i in range(5):
    print(i)


# In[35]:


# find square of numbers
for i in range(3):
    num = int(input("Enter number: "))
    print("The square of your number:",num*num)
print("The loop is done")


# In[39]:


print('A')
print('B')
for i in range(5):
    print('C')
for i in range(3):
    print('D')
print('E')


# In[41]:


print('A')
print('B')
for i in range(5):
    print('C')
    print('D')
print('E')


# In[43]:


s = input("Please type some character: ")
for c in s:
    print(c)
print("done")


# In[44]:


for i in range(4):
    print('*'*5)


# In[47]:


for i in range(5): # 0,1,2,3,4
    print('*'*(i+1))


# In[48]:


# converted to string
x = 10
y = 20 
print(str(x)+ str(y))


# In[49]:


# using a nested loop number 
for i in range(10):  # 0,1,2,...,9
    print(str(i)*i)


# In[56]:


# multiplication table
num = int(input("Enter a number: "))
for i in range(1,11):
    print(num, "x", i, "=",num*i)


# In[ ]:




