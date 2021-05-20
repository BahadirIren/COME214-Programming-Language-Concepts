#!/usr/bin/env python
# coding: utf-8

# In[10]:


# math equation example
import math
x = int(input("Enter x: "))

y = (x + (math.sqrt(x + 4))) / (pow(x,2) + pow(x + 2, 1/3))

print(y)
print(format(y,".2f"))


# In[13]:


# math equation example
import math
x = int(input("Enter x: "))

if x <= 5 :
    y = x / (pow(x,2) + 2)
else:
    y = x / (1 + (math.sqrt(x + 1)))

print(y)
print(format(y,".2f"))


# In[14]:


# discriminant example
import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c : "))

delta = pow(b,2) - 4*a*c

if delta < 0 :
    print("There is no real root")
elif delta == 0:
    x1 = -b / 2*a
    x2 = x1
    print(x1)
    print(x2)
else :
    x1 = (-b + math.sqrt(delta)) / 2*a
    x2 = (-b - math.sqrt(delta)) / 2*a
    print(x1)
    print(x2)


# In[16]:


# summation 1+2+....+N
N = int(input("Enter n: "))
sum = 0
for i in range(1,N+1):
    sum += i
print(sum)


# In[22]:


# multiplication table
n = int(input("Enter n: "))
for i in range(1,11):
    print(n*i)


# In[55]:


# prime number
num = int(input("Enter integer number: "))

if num == 1:
    print("1 is not prime number")
else:
    for i in range(2,num):
        if num % i == 0:
            prime = False
            break     # when it found it is not prime, exit the loop otherwise it won't work properly
        else:
            prime = True
    if prime:
        print(num,"is prime number")
    else:
        print(num,"is not prime number")


# In[76]:


# factorial 
num = int(input("Enter integer number: "))
factorial = 1

if num < 0:
    print("Enter positive number")
else:
    for i in range(2, num+1):
        factorial *= i
    print("factorial of",num, "is", factorial)


# In[ ]:




