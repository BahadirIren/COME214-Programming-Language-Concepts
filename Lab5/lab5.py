#!/usr/bin/env python
# coding: utf-8

# In[21]:


for i in range(1,4):
    for j in range(1,3):
        print(i,",",j)


# In[15]:


for x in range(1,6):
    for y in range(1,6):
        result = (x+y)/(pow(x,3)*y + pow(y,2))
        print("f(",x,",",y,") =",format(result,".2f"))


# In[30]:


for x in range(1,6):
    for y in range(1,6):
        result = (x+y)/(pow(x,3)*y + pow(y,2))
        print("f(",x,",",y,") =",format(result,".2f"),"\t",end= "")


# In[62]:


# multiplication table
n = int(input("Enter a number: "))

for i in range(1,n+1):
    print("\t",i,"\t",end=" ")
print()
for i in range(1,n+1):
    print("---------------",end=" ")
print()
for i in range(1,n+1):
    print(i,"|",end=" ")
    for j in range(1,n+1):
        print("\t",i*j,"\t",end=" ")
    print()
        


# In[85]:


# sum of the series
n = int(input("Enter a number: "))

start = "2"
sum = 0
series= start
for i in range(1,n+1):
    sum += int(start*i)
    series += (" + " + str(start*i))
print()
print(series)
print("Sum of the series is=",sum)


# In[88]:


# sum of the series
number_of_terms = 5
start = 2
sum = 0

for i in range(1,number_of_terms +1):
    print(start,end=" ")
    if i != number_of_terms:
        print("+",end=" ")
    sum += start
    start = start*10 +2
    
print()
print("The sum of the above series is=", sum)


# In[103]:


# finding interests
import math
invested = 10000
rate = 0.05
total_years = 10

for year in range(1,total_years +1):
    deposit = invested*pow(1+rate,year)
    print("After",year,"year", "\t",format(deposit,".2f"),"$")


# In[107]:


# random number
import random

print(random.randrange(1,7))


# In[113]:


from random import randint

rand_number = randint(5,15)
for i in range(rand_number):
    print("hello")


# In[8]:


# dice example
'''
Roll a six-sided die 6,000,000 times.
Each dies face 1-6 occur with equal likehood, the following script simulates 6,000,000 die (6 million)
Die rolls. When you run the script,each die face should occur approximately 1,000,000 times , as in the sample output. 
 
Print Frequency of face 
Print Probability of face 

It finished about 12-13 seconds
'''
from random import randint

times = 6000000

# define frequency and initialize to 0
for i in range(1,7):
    globals()["frequency{}".format(i)] = 0

# count frequency
for i in range(1, times +1):
    rand_number = randint(1,6)
    for face in range(1,7):
        if face == rand_number:
            globals()["frequency{}".format(face)] += 1
            
# print frequency and probability
for i in range(1,7):
    print("Frequency of face {}:".format(i),globals()["frequency{}".format(i)],"and Probability:",format(globals()["frequency{}".format(i)]/times,".4f" ))
        


# In[9]:


# dice example
'''
Roll a six-sided die 6,000,000 times.
Each dies face 1-6 occur with equal likehood, the following script simulates 6,000,000 die (6 million)
Die rolls. When you run the script,each die face should occur approximately 1,000,000 times , as in the sample output. 
 
Print Frequency of face 
Print Probability of face 

It finished about 5-6 seconds
'''
import random

times = 6000000

# define frequency and initialize to 0
frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0

# count frequency
for i in range(1, times+1):
    rand_number = random.randrange(1,7)
    if rand_number == 1:
        frequency1 += 1
    elif rand_number == 2:
        frequency2 += 1
    elif rand_number == 3:
        frequency3 += 1
    elif rand_number == 4:
        frequency4 += 1
    elif rand_number == 5:
        frequency5 += 1
    elif rand_number == 6:
        frequency6 += 1

# print frequency and probability
for i in range(1,7):
    print("Frequency of face {}:".format(i),globals()["frequency{}".format(i)],"and Probability:",format(globals()["frequency{}".format(i)]/times,".4f" ))


# In[ ]:




