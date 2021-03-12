#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
print(math.sqrt(25))


# In[10]:


print(dir(math))


# In[2]:


print(help(math))


# In[3]:


a = 9.8
b = math.ceil(a) # returns the smallest int value which is greater than number
print(b)


# In[4]:


a = 9.8
b = math.floor(a) # returns the biggest int value which is smaller than number
print(b)


# In[5]:


print(math.factorial(5))


# In[7]:


print(math.trunc(78.98))  # ignore decimal points


# In[18]:


# by default base is e
print("natural logarithm of e =", math.log(math.e)) # lne = 1
print("loagatihm base 5 of 14 is =", math.log(14,5)) # log5(14)
print("loagatihm base 10 of 14 is =", math.log(14,10)) # log10(14)
print("loagatihm base 10 of pi is =", math.log(math.pi,10)) 
print("loagatihm base 10 of pi is =", math.log10(math.pi))


# In[19]:


print(math.pow(3,2))


# In[34]:


# example1 : assume we want to see if a number entered by a user is divisible by 7
num = int(input("Enter an integer number: "))

if num % 7 == 0 :
    print("Entered number" ,num ,"is divisible by 7")
else :
    print("Entered number", num, "is not divisible by 7")


# In[38]:


# example2 : write a program to find the lowest number out of two numbers from user

num1 = int(input("Enter an integer number: "))
num2 = int(input("Enter an integer number: "))

if num1 > num2 :
    print(num1, "is greater than" , num2)
elif num1 < num2:
    print(num1, "is less than" , num2)
else : 
    print(num1, "is equal to", num2)


# In[53]:


# example3 : find the greatest number of three numbers

num1 = int(input("Enter an integer number: "))
num2 = int(input("Enter an integer number: "))
num3 = int(input("Enter an integer number: "))

if num1 > num2 and num1 > num3 :
    print(num1)
elif num2 > num3 :
    print(num2)
else :
    print(num3)


# In[56]:


# example3 : guess and check pattern

x = int(input("Enter an integer number: "))
y = int(input("Enter an integer number: "))
z = int(input("Enter an integer number: "))

maxNum = x  # here is our initial guess

if y > maxNum :
    maxNum = y
if z > maxNum :
    maxNum = z
    
print(maxNum)
    


# In[59]:


# example4 : write a program checks whether a number is even or odd

x = int(input("Enter an integer number: "))

if x % 2 == 0 :
    print(x, "is even")
else:
    print(x, "is odd")


# In[61]:


# example5 : consider a club where you must under 18 and over 15 to join

age = int(input("Enter your age: "))

if (not age > 15) or  (not age < 18) :
    print("you can not join")
else :
    print("you can join")


# In[63]:


# example5 : consider a club where you must under 18 and over 15 to join (guess and check pattern)

age = int(input("Enter your age: "))

check = True

if age <= 15 :
    check = False
if age >= 18 :
    check = False
    
if check :
    print("you can join")
else :
    print("you can`t join")


# In[71]:


# example6 : score example

grade = int(input("Enter your score: "))

if grade >= 90 :
    print("A")
elif grade >= 80 :
    print("B")
elif grade >= 70 :
    print("C")
elif grade >= 60 :
    print("D")
elif grade >= 50 :
    print("E")
else:
    print("F")
    


# In[90]:


# example7 : write a program accept a number from 1 to 7 and display the name of the day like 1 for Monday so on

day = int(input("Enter number 1 to 7: "))


if day == 1 :
    print("Monday")
elif day == 2 :
    print("Tuesday")
elif day == 3 :
    print("Wednesday")
elif day == 4 :
    print("Thursday")
elif day == 5 :
    print("Friday")
elif day == 6 :
    print("Saturday")
elif day == 7 :
    print("Sunday")
else :
    print("Wrong number entered! , enter 1 to 7")
        


# In[ ]:




