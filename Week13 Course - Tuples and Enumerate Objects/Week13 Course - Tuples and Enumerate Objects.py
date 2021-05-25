#!/usr/bin/env python
# coding: utf-8

# In[1]:


colors = ["red", "green", "blue"]
print(colors)
print(colors[0])

print(enumerate(colors))
print(list(enumerate(colors)))
print(list(enumerate(colors,10)))


# In[2]:


colors = ["red", "green", "blue"]

for index, value in enumerate(colors,1):
    print(f"{index}: {value}")


# In[7]:


x = 5 
y = 10

print(f"{x}")
print(f"{x:>10} {y:>8}") # put empty space

print(f"{'Hello':>20}")  # same you must use single quote
print("               Hello") # same


# In[15]:


# create a primitive a bar chart

numbers = [19, 3,15,7,11]

print(f"Index {'Value':>8}  Bar")

for index,value in enumerate(numbers):
    print(f"{index:>5} {value:>8}  {'?'*value}")
    


# In[21]:


# Lists
colors = ["red", "green", "blue"] # mutable
colors[0] = "black"
print(colors)

# Tuples

student_tuple = ("Jhon", "Green", 100) # immutable
print(len(student_tuple))
print(student_tuple)
print(student_tuple[2])

time_tuple = (9,16,1)
print(time_tuple[0]*3600 + time_tuple[1]*60 + time_tuple[2])


# In[24]:


# unpacking process

student_tuple = ("Jhon", "Green", 100)
name,surname,grade = student_tuple

print(name)
print(surname)
print(grade)


# In[26]:


my_list = list(range(1,16))

print(my_list)

my_tuple = tuple(range(1,16))

print(my_tuple)


# In[29]:


a = [[77,56,34,12],[23,99,61,43],[34,62,16,73]]

for row in a:
    for item in row:
        print(item, end=" ")
    print()   


# In[50]:


a = [[77,56,34,12],[23,99,61,43],[34,62,16,73]]

for i,row in enumerate(a):
    for j, item in enumerate(row):
        print(f"a[{i}][{j}] = {item}",end= "\t")
    print()


# In[ ]:




