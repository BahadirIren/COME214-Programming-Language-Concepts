#!/usr/bin/env python
# coding: utf-8

# In[8]:


# define function which finds prime number between give two numbers

def prime(num1, num2):
    for number in range(num1, num2+1):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                print(number, end=" ")
                
                
prime(3,12)


# In[32]:


L = [1,2,3,4]
L = [1,"Hello",3,4]
L = [1,2,3,[1,"Hello",3,4]]  # nested list
my_list = ["p", "r", "o","g", "r", "a", "m", "m", "i", "n", "g"]
print(my_list)
print("".join(my_list))
print(my_list[2])
print(my_list[-2])
print(my_list[2:5])


# In[21]:


odd = [2,4,6,8]
odd[0] = 1
print(odd)
odd[1:4] = [3,5,7]
print(odd)

odd.append(9)
print(odd)

odd.extend([11,13])
print(odd)

print(odd + [15,17])
print([odd]*2)
print(["*"]*3)


# In[28]:


x = [1,2,3,4,5,6,7,8,9]
print(x[::2]) # prints odd numbers
print(x[1::2]) # prints even numbers


# In[30]:


list1 = [1,2,3]
list2 = ["red","white","blue"]

list = list1 + list2
print(list)


# In[47]:


odd = [1,3,5]

odd.insert(1,9)
print(odd)
odd[2:2] = [7,11]
print(odd)


# In[48]:


my_list = ["p", "r", "o","g", "r", "a", "m", "m", "i", "n", "g"]

del my_list[2]
print(my_list)

del my_list[2:4]
print(my_list)

my_list.remove("p")
print(my_list)


# In[1]:


num = [30,12,40,-5]

print(num.index(12))


# In[2]:


num = [30,12,40,-5]

for a in num:
    print(a)


# In[3]:


num = [30,12,40,-5]

for a in range(len(num)):
    print(num[a])


# In[5]:


num = [30,12,5,40,-5]

if 5 in num:
    print("Your list contains 5")
if 0 not in num:
    print("Your list has no 0")


# In[6]:


for fruit in ["apple", "banana","cherry"]:
    print("I like", fruit)


# In[8]:


num = [30,12,5,40,-5]

print(5 in num)
print(0 in num)


# In[10]:


list = []
for i in range(10):
    list.append(2**i)
print(list)


# In[20]:


list = [2**i for i in range(10)]
print(list)


# In[13]:


list = [2**x for x in range(6,10)]
print(list)


# In[17]:


list = [2**x for x in range(10) if x > 5]
print(list)


# In[19]:


list = [x for x in range(30) if x % 2 == 1]
print(list)


# In[28]:


list = ["p","q"]
n = 4
new_list = [f"{i}{j}"  for j in range(1,n+1) for i in list]
print(new_list)


# In[57]:


list1 = ["Python", "C"]
list2 = ["Programming", "Language"]

new_list = [f"{i} {j}" for i in list1 for j in list2]

print(new_list)


# In[58]:


new_list = [i +" "+ j for i in ["Python", "C"] for j in ["Programming", "Language"]]

print(new_list)


# In[32]:


def list_sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(list_sum([1,2,3,4,5]))


# In[34]:


import random
list = [random.randrange(1,101) for i in range(10)]
print(list)


# In[59]:


import random
list = [random.randrange(1,101) for i in range(10)]

count = 0
for j in list:
    if j > 50:
        count += 1

print(list)
print(count)


# In[ ]:




