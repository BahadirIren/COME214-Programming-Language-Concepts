#!/usr/bin/env python
# coding: utf-8

# In[8]:


n = int(input("Enter the number of characters that you want to print: "))

while n != -1:
    ch = input("\nEnter a character: ")
    for i in range(1, n+1):
        print(ch, end=" ")
    print()
    n = int(input("\nEnter the number of characters that you want to print: "))
    if n == -1:
        print("\nProgram is finished!")


# In[31]:


# ulam sequence
n = int(input("Enter a number: "))

while n != 1:
    if n % 2 == 1:
        print(n , "->", end=" ")
        n = n * 3 + 1
    else:
        print(n , "->", end=" ")
        n = n // 2
        if n == 1:
            print(1)  


# In[58]:


# fibonacci

n1 = 0
n2 = 1
count = 0

while count < 20:
    print(n1,end=" ")
    temp = n1 + n2
    n1 = n2
    n2 = temp
    count += 1


# In[60]:


# fibonacci 

a,b = 0,1
print(a,b,end=" ")

i = 1
while i <= 18:
    a,b = b,a+b
    print(b,end=" ")
    i += 1


# In[44]:


num = int(input("How many fibonacci numbers do you want to see?: "))

a,b = 0,1
print(a,b,end=" ")

i = 1
while i <= num - 2:
    a,b = b,a+b
    print(b,end=" ")
    i += 1


# In[47]:


a = (2,3,4)
print(min(a))
print(min(65,12))


# In[56]:


# Greater Common Divisor

num1 = int(input("Enter a positive integer number: "))
num2 = int(input("Enter a positive integer number: "))

divisor = min(num1,num2)

while num1 % divisor != 0 or num2 % divisor != 0:
    divisor -= 1
    
print(f"The greatest common divisor of {num1} and {num2} is: {divisor}")


# In[ ]:




